import os
import shutil

def copy_files_without_wav(src_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Iterate over all files in the source directory
    for filename in os.listdir(src_dir):
        # Construct full file path
        src_file = os.path.join(src_dir, filename)

        # Check if it is a file and not a ".wav" file
        if os.path.isfile(src_file) and not filename.lower().endswith('.wav') and not filename.lower().endswith('.mp3') and not filename.lower().endswith('.flac') and not filename.lower().endswith('.aac') and not filename.lower().endswith('.ogg'):
            # Construct the destination file path
            dest_file = os.path.join(dest_dir, filename)
            # Copy the file
            shutil.copy(src_file, dest_file)
            print(f"Copied {src_file} to {dest_file}")

# Example usage
source_directory = '/workspace/Codec-SUPERB/ref_path'
destination_directory = '/workspace/Codec-SUPERB/syn_path'

copy_files_without_wav(source_directory, destination_directory)
