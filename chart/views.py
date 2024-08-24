# views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from pydicom.dataset import Dataset
from pydicom.uid import generate_uid
from PIL import Image
import numpy as np
import os

def png_to_dcm(request):
    if request.method == 'POST' and 'png_file' in request.FILES:
        # Handle file upload
        png_file = request.FILES['png_file']
        fs = FileSystemStorage()
        filename = fs.save(png_file.name, png_file)
        file_path = fs.path(filename)

        # Convert PNG to DICOM
        image = Image.open(file_path)
        pixel_data = np.array(image)

        # Create DICOM dataset
        ds = Dataset()
        ds.file_meta = Dataset()
        ds.file_meta.MediaStorageSOPClassUID = generate_uid()
        ds.file_meta.MediaStorageSOPInstanceUID = generate_uid()
        ds.file_meta.ImplementationClassUID = generate_uid()

        # Set required values
        ds.PatientName = "Test^Name"
        ds.PatientID = "123456"
        ds.Rows, ds.Columns = pixel_data.shape[:2]  # Adjust for 2D data
        ds.SamplesPerPixel = 1
        ds.PhotometricInterpretation = "MONOCHROME2"
        ds.BitsAllocated = 8
        ds.BitsStored = 8
        ds.HighBit = 7
        ds.PixelRepresentation = 0
        ds.PixelData = pixel_data.tobytes()

        # Set endianness and VR encoding
        ds.is_little_endian = True
        ds.is_implicit_VR = True

        # Save as DICOM file
        dcm_filename = filename.replace('.png', '.dcm')
        dcm_path = os.path.join(fs.location, dcm_filename)
        ds.save_as(dcm_path)

        # Return the DICOM file as a download
        with open(dcm_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/dicom')
            response['Content-Disposition'] = f'attachment; filename="{dcm_filename}"'
            return response

    return render(request, 'index.html')
