import csv
from django.shortcuts import render, redirect
from .models import Records
from .forms import UploadFileForm

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_csv(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file'].read().decode('utf-8').splitlines()
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                name = f"{row[0]} {row[1]}"
                for cls in [row[2], row[3]]:
                   Records.objects.create(
                        name=name,
                        class_name=cls,
                        school=row[4],
                        state=row[5]
                    )
            return redirect('success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')