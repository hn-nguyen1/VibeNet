from datetime import datetime


class Post:
    """
    A class representing a social media post in the VibeNet platform.
    """

    def __init__(self, post_id, user_id, content, like_count=0, comment_count=0, comments=None, date=None):
        self.post_id = post_id
        self.user_id = user_id
        self.content = content
        self.like_count = like_count
        self.comment_count = comment_count
        if comments is None:
            self.comments = []
        else:
            self.comments = comments
        self.date = datetime.strptime(date, '%Y-%m-%d') if date else datetime(2025, 4, 14)
        self.author = None

    def get_engagement_score(self):
        return self.like_count * 0.5 + self.comment_count * 1.0

    def edit_content(self, new_content, editor_id):
        if not new_content or self.user_id != editor_id:
            return False
        self.content = new_content
        return True

    def can_modify(self, user_id):
        return self.user_id == user_id

    def __str__(self):
        author_str = f"Author: {self.author}" if self.author else f"User ID: {self.user_id}"
        if self.comment_count == 0:
            return f"\tPost ID: {self.post_id}\n\t{author_str}\n\tDate: {self.date.strftime('%Y-%m-%d')}\n\tContent: {self.content}\n\tLikes: {self.like_count}\n\tTotal Comments: {self.comment_count}\n"
        else:
            comment_str = "\n".join([f"\t\t{comment}" for comment in self.comments])
            return f"\tPost ID: {self.post_id}\n\t{author_str}\n\tDate: {self.date.strftime('%Y-%m-%d')}\n\tContent: {self.content}\n\tLikes: {self.like_count}\n\tTotal Comments: {self.comment_count}\n\tComments:\n{comment_str}\n"

    def __repr__(self):
        return f"Post(post_id='{self.post_id}', user_id='{self.user_id}', content='{self.content}', like_count={self.like_count}, comment_count={self.comment_count}, date='{self.date.strftime('%Y-%m-%d')}')"


class User:
    """
    A class representing a user in the VibeNet platform.
    """

    def __init__(self, user_id, username, password, followers=0, following=0):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.followers = followers
        self.following = following
        self.posts = {}

    def display_profile(self):
        print("\nUser Profile:")
        print("=" * 50)
        print(self)
        print("=" * 50)

        if self.posts:
            print("\nUser Posts:")
            print("=" * 50)
            for _, post in self.posts.items():
                print(post)
                print("=" * 50)
        else:
            print("\nNo posts yet.")

    def __str__(self):
        return f"\tUser ID: {self.user_id}\n\tUsername: {self.username}\n\tFollowers: {self.followers}\n\tFollowing: {self.following}\n"

    def __repr__(self):
        return f"User(user_id='{self.user_id}', username='{self.username}', password='***', followers={self.followers}, following={self.following})"


class VibeNet:
    """
    The main class for the VibeNet social media platform.
    """

    def __init__(self):
        self.users = {}
        self.posts = {}

    def read_users_file(self, filename):
        fp_users = open(filename, 'r')
        next(fp_users)
        for line in fp_users:
            user_id, username, password, followers, following = line.strip().split(',')
            self.users[user_id] = User(user_id, username, password, int(followers), int(following))

    def read_posts_file(self, file_posts, file_comments):
        fp_posts = open(file_posts, 'r')
        next(fp_posts)
        for line in fp_posts:
            post_id, user_id, content, like_count, comment_count, date = line.strip().split(',')
            like_count = int(like_count)
            comment_count = int(comment_count)
            post = Post(post_id, user_id, content, like_count, comment_count, None, date)
            post.author = self.users[user_id].username
            self.posts[post_id] = post
            self.users[user_id].posts[post_id] = post
        fp_posts.close()

        fp_comments = open(file_comments, 'r', encoding="UTF-8")
        next(fp_comments)
        for line in fp_comments:
            post_id, user_id, comment = line.strip().split(',')
            post = self.posts[post_id]
            post.comments.append(f"{user_id}: {comment}")
        fp_comments.close()

    def search_posts_by_date(self, start_date, end_date):
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            end = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return None

        matching_posts = [
            post for post in self.posts.values()
            if start <= post.date <= end
        ]
        matching_posts.sort(key=lambda x: x.date, reverse=True)
        return matching_posts

    def add_user(self, username, password):
        next_id = str(max(int(user_id) for user_id in self.users.keys()) + 1) if self.users else "1"
        new_user = User(next_id, username, password, 0, 0)
        self.users[next_id] = new_user
        return new_user

    def add_post(self, user_id, content):
        if not content:
            return None
        next_post_id = str(len(self.posts) + 1)
        new_post = Post(next_post_id, user_id, content)
        new_post.author = self.users[user_id].username
        self.posts[next_post_id] = new_post
        self.users[user_id].posts[next_post_id] = new_post
        return new_post

    def display_user_posts(self, user_id):
        user_posts = [post for post in self.posts.values() if post.user_id == user_id]
        if user_posts:
            print("\nYour Posts:")
            print("=" * 50)
            for post in user_posts:
                print(post)
                print("=" * 50)
        else:
            print("\nYou haven't created any posts yet.")

    def get_user(self, user_id):
        return self.users[user_id]
