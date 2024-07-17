import os
import shutil


def copy_files_without_wav(src_dir, dest_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Walk through the source directory
    for root, dirs, files in os.walk(src_dir):
        # Create corresponding subdirectories in the destination directory
        for dir_name in dirs:
            src_subdir = os.path.join(root, dir_name)
            dest_subdir = os.path.join(dest_dir, os.path.relpath(src_subdir, src_dir))
            if not os.path.exists(dest_subdir):
                os.makedirs(dest_subdir)
        
        # Copy files, excluding .wav files
        for file_name in files:
            if not file_name.lower().endswith('.wav') and not file_name.lower().endswith('.mp3') and not file_name.lower().endswith('.flac') and not file_name.lower().endswith('.aac') and not file_name.lower().endswith('.ogg'):
                src_file = os.path.join(root, file_name)
                dest_file = os.path.join(dest_dir, os.path.relpath(src_file, src_dir))
                dest_file_dir = os.path.dirname(dest_file)
                
                # Create the directory if it doesn't exist
                if not os.path.exists(dest_file_dir):
                    os.makedirs(dest_file_dir)
                
                shutil.copy2(src_file, dest_file)
                print(f"Copied {src_file} to {dest_file}")


# Example usage
source_directory = '/workspace/Codec-SUPERB/ref_path'
destination_directory = '/workspace/Codec-SUPERB/syn_path'

copy_files_without_wav(source_directory, destination_directory)
