import zipfile

#Create a ZIP file
with zipfile.ZipFile('coding_challenge.py', 'w') as zip_file:
    # Add a file to the ZIP archive
    zip_file.write('coding _challenge.py')

# Close the ZIP file
zip_file.close()