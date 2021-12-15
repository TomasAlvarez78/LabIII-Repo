import glob

print("aa")

# jpgFilenamesList = glob.glob('media/categoriaImagenes/1*.jpg')

for i in range (10):
    jpgFilenamesList = glob.glob(f'media/categoriaImagenes/{i+1} -*.jpg')[0]
    print(jpgFilenamesList)
