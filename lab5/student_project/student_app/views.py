from django.shortcuts import render

# Create your views here.


def student_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        contact_no = request.POST.get('contact_no')
        email = request.POST.get('email')
        eng_marks = float(request.POST.get('eng_marks'))
        phy_marks = float(request.POST.get('phy_marks'))
        chem_marks = float(request.POST.get('chem_marks'))
        total_marks = eng_marks + phy_marks + chem_marks
        percentage = (total_marks / 300) * 100
        student_info = f"Name: {name}\nDate of Birth: {dob}\nAddress: {address}\nContact Number: {contact_no}\nEmail ID: {email}\nEnglish Marks: {eng_marks}\nPhysics Marks: {phy_marks}\nChemistry Marks: {chem_marks}\nPercentage: {percentage}%\n"
        return render(request, 'student_details.html', {'student_info': student_info})
    else:
        return render(request, 'student_details.html')
