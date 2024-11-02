import os
from instagrapi import Client

# Ask for user input for the folder path, username, and password
video_folder = input("Enter the path to your video folder: ")
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

# Authenticate with Instagram
client = Client()
try:
    client.login(username, password)
    print("Login successful!")
except Exception as e:
    print(f"Login failed: {e}")
    exit()

def upload_reels_from_folder(folder_path):
    # Get all files in the folder
    for video_file in os.listdir(folder_path):
        # Check if it's a video file (add more extensions if needed)
        if video_file.endswith(('.mp4', '.mov', '.avi')):
            video_path = os.path.join(folder_path, video_file)
            print(f"Found file: {video_path}")
            
            caption = "The Tesla Cybertruck is an all-elelctric,se Battery-powered light-duty truck unveiled by Tesla, Inc,Here's a comprehensive overview of its key features and specification:Tesla Cybertruck OverviewDesign in Structure• Exterior: The cybershrak has a distinctive,angular stainless steel exoskeleton design for durability and passenger protection. It featured ultra-hard 30X colled-rolled stainless steel and armoured glass.• Dimensions: approximately 231.7 inches long, 79.8 inches wide. and 75 inches tall, with 6.5-foot cargo bed.Performance and Variants• Single Motor RWD:• 0-60 mph: ~6.5 seconds• Range: ~250 miles• Towing Capacity: 7,500 pounds• Dual Motor AWD:• 0-60 mph: ~4.5 seconds• Range: ~300 milesal • Towing Capacity: 10,000 pounds• Tri-Motor AWD:• 0-60 mph: ~2.9 seconds• Range: ~500 miles• Towing Capacity: 14,000 pounds•#instagramgrowth•#igrich •#explore •#instagramhack •#trending •#bhojpuri •#reels"  # Customize as needed
            
            # Upload video as a reel
            try:
                client.clip_upload(video_path, caption=caption)
                print(f"Uploaded {video_file} successfully.")
            except Exception as e:
                print(f"Failed to upload {video_file}: {e}")

# Run the upload function
upload_reels_from_folder(video_folder)

# Logout after uploading all videos
client.logout()
print("Logged out successfully!")
