from vibenet import VibeNet


def validate_password(password):
    """Validate password requirements."""
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(not char.isalnum() for char in password):
        return False
    return True


def login_user(vibenet):
    """Prompt for credentials and return the authenticated user."""
    user_id = input(":~Enter user ID ~:")
    if user_id not in vibenet.users:
        print("Error: User ID not found.")
        return None

    password = input(":~Enter password ~:")
    user = vibenet.users[user_id]

    if user.password == password:
        print(f"Successfully logged in as {user.username}")
        return user

    print("Error: Incorrect password.")
    return None


def signup_user(vibenet):
    """Create a new user account."""
    username = input(":~Enter username ~:")

    while True:
        password = input(":~Enter password ~:")
        if validate_password(password):
            break
        print("Error: Invalid password.")

    new_user = vibenet.add_user(username, password)
    print("User created successfully!")
    new_user.display_profile()
    return new_user


def create_post(vibenet, user):
    """Create a new post."""
    content = input(":~Enter your post content ~:")

    if not content.strip():
        print("Post content cannot be empty.")
        return

    new_post = vibenet.add_post(user.user_id, content)

    if new_post:
        print(f"Post created successfully! Post ID: {new_post.post_id}")
    else:
        print("Failed to create post.")


def view_profile(vibenet, user):
    """Display the user's profile and post-management options."""
    user.display_profile()

    if not user.posts:
        return

    while True:
        print("\nPost Management:")
        print("\t1. Edit Post")
        print("\t2. Delete Post")
        print("\t3. Back to Menu")

        choice = input(":~Enter your choice (1-3) ~:")

        if choice == "1":
            edit_post(vibenet, user)
            return
        elif choice == "2":
            delete_post(vibenet, user)
            return
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter 1-3.")


def edit_post(vibenet, user):
    """Edit an existing post owned by the current user."""
    post_id = input(":~Enter post ID to edit ~:")

    if post_id not in vibenet.posts:
        print("Post not found.")
        return

    post = vibenet.posts[post_id]

    if not post.can_modify(user.user_id):
        print("You can only edit your own posts.")
        return

    print(f"\nCurrent content: {post.content}")
    new_content = input(":~Enter new content ~:")

    if not new_content.strip():
        print("Failed to update post. Content cannot be empty.")
        return

    if post.edit_content(new_content, user.user_id):
        print("Post updated successfully!")
    else:
        print("Failed to update post. Invalid content or permissions.")


def delete_post(vibenet, user):
    """Delete an existing post owned by the current user."""
    post_id = input(":~Enter post ID to delete ~:")

    if post_id not in vibenet.posts:
        print("Post not found.")
        return

    post = vibenet.posts[post_id]

    if not post.can_modify(user.user_id):
        print("You can only delete your own posts.")
        return

    del vibenet.posts[post_id]
    if post_id in user.posts:
        del user.posts[post_id]

    print("Post deleted successfully!")


def search_posts_by_tag(vibenet):
    """Search for posts containing a specified hashtag."""
    tag = input(":~Enter tag to search (without #) ~:").strip()

    if not tag:
        print("Tag cannot be empty.")
        return

    matching_posts = [
        post for post in vibenet.posts.values()
        if f"#{tag.lower()}" in post.content.lower()
    ]

    if matching_posts:
        matching_posts.sort(key=lambda post: post.date)
        print(f"\nFound {len(matching_posts)} post(s) with #{tag}:")
        print("=" * 50)

        for post in matching_posts:
            print(post)
            print("=" * 50)
    else:
        print(f"No posts found with #{tag}")


def view_newsfeed(vibenet, user):
    """Display posts sorted by engagement score and date."""
    posts_with_scores = [
        (post, post.get_engagement_score())
        for post in vibenet.posts.values()
    ]

    sorted_posts = sorted(
        posts_with_scores,
        key=lambda item: (item[1], item[0].date),
        reverse=True
    )

    print("\nNewsfeed (Sorted by Engagement & Date):")
    print("=" * 50)

    for post, score in sorted_posts:
        print(post)
        print(f"\tEngagement Score: {score}")
        print("=" * 50)

    while True:
        print("\nPost Menu")
        print("\t1. Like Post")
        print("\t2. Comment on Post")
        print("\t3. Back to User Menu")

        choice = input(":~Enter your choice (1-3) ~:")

        if choice == "1":
            like_post(vibenet, user)
            return
        elif choice == "2":
            comment_on_post(vibenet, user)
            return
        elif choice == "3":
            return
        else:
            print("Invalid choice. Please enter 1-3.")


def like_post(vibenet, user):
    """Add a like to a post."""
    post_id = input(":~Enter post ID to like ~:")

    if post_id in vibenet.posts:
        vibenet.posts[post_id].like_count += 1
        print("Like added successfully!")
    else:
        print("Post not found.")


def comment_on_post(vibenet, user):
    """Add a comment to a post."""
    post_id = input(":~Enter post ID to comment on ~:")

    if post_id not in vibenet.posts:
        print("Post not found.")
        return

    comment = input(":~Enter your comment ~:")

    if not comment.strip():
        print("Comment cannot be empty.")
        return

    post = vibenet.posts[post_id]
    post.comments.append(f"{user.username}: {comment}")
    post.comment_count += 1

    print("Comment added successfully!")


def view_users(vibenet):
    """Display users sorted by follower and following counts."""
    all_users = list(vibenet.users.values())
    all_users.sort(
        key=lambda user: (user.followers, user.following),
        reverse=True
    )

    print("\nVibeNet Users")
    print("=" * 50)

    for user in all_users:
        print(user)
        print("=" * 50)


def search_posts_by_date(vibenet):
    """Search for posts within a specified date range."""
    print("\nEnter date range (format: YYYY-MM-DD)")
    start_date = input(":~Start date ~:")
    end_date = input(":~End date ~:")

    matching_posts = vibenet.search_posts_by_date(start_date, end_date)

    if matching_posts:
        print(f"\nFound {len(matching_posts)} posts between {start_date} and {end_date}:")
        print("=" * 50)

        for post in matching_posts:
            print(post)
            print(f"\tEngagement Score: {post.get_engagement_score()}")
            print("=" * 50)
    else:
        print(f"No posts found between {start_date} and {end_date}")


def user_menu(vibenet, user):
    """Display the authenticated user's main menu."""
    while True:
        print("\nVibeNet Menu")
        print("\t1. Create Post")
        print("\t2. View Profile")
        print("\t3. Search Posts by Tag")
        print("\t4. View Newsfeed")
        print("\t5. View Users")
        print("\t6. Search Posts by Date")
        print("\t7. Log Out")

        choice = input(":~Enter your choice (1-7) ~:")

        if choice == "1":
            create_post(vibenet, user)
        elif choice == "2":
            view_profile(vibenet, user)
        elif choice == "3":
            search_posts_by_tag(vibenet)
        elif choice == "4":
            view_newsfeed(vibenet, user)
        elif choice == "5":
            view_users(vibenet)
        elif choice == "6":
            search_posts_by_date(vibenet)
        elif choice == "7":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please enter 1-7.")


def main():
    banner = """🌟 Welcome to VibeNet! 🌟
A place where good vibes, great convos,
and awesome people come together.
Settle in, explore, and let the vibes find you! 🎶💫"""

    user_file = "users.txt"
    posts_file = "posts.txt"
    comments_file = "post_comments.txt"

    vibenet = VibeNet()
    vibenet.read_users_file(user_file)
    vibenet.read_posts_file(posts_file, comments_file)

    while True:
        print(banner)
        print("\t1. Log in")
        print("\t2. Sign up")
        print("\t3. Exit")

        choice = input(":~Enter your choice (1-3) ~:")

        if choice == "1":
            user = login_user(vibenet)
            if user:
                user_menu(vibenet, user)
        elif choice == "2":
            user = signup_user(vibenet)
            if user:
                user_menu(vibenet, user)
        elif choice == "3":
            print("The vibes don't stop, and neither do we! Thank you for using VibeNet...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
