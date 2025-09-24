import os
import shutil

user = os.getenv('USER')

print(os.environ)
root_dir = f'/Users/{user}/Downloads/'
image_dir = '/Users/{}/Downloads/images/'.format(user)
document_dir = '/Users/{}/Downloads/documents/'.format(user)
others_dir = '/Users/{}/Downloads/others/'.format(user)
software_dir = '/Users/{}/Downloads/software/'.format(user)

doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', 'xlsx', '.pptx')
img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif', '.tif', '.tiff')
software_types = ('.exe', '.pkg', '.dmg')

def OrganizeDirectory(root_dir):
    return [f for f in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, f)) and not f.startswith('.') and not f == __file__]

def move_files(files):
    for file in files:
        if file.endswith(doc_types):
            shutil.move(os.path.join(root_dir, file), os.path.join(document_dir, file))
            print('file {} moved to {}'.format(file, document_dir))
        elif file.endswith(img_types):
            shutil.move(os.path.join(root_dir, file), os.path.join(image_dir, file))
            print('file {} moved to {}'.format(file, image_dir))
        elif file.endswith(software_types):
            shutil.move(os.path.join(root_dir, file), os.path.join(software_dir, file))
            print('file {} moved to {}'.format(file, software_dir))
        else:
            shutil.move(os.path.join(root_dir, file), os.path.join(others_dir, file))
            print('file {} moved to {}'.format(file, others_dir))

if __name__ == "__main__":
    files = OrganizeDirectory(root_dir)
    move_files(files)
