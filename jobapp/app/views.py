from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect
from django.urls import reverse
job_title = [
    "Control Engineer",
    "Electrical Engineer",
    "Software Engineer", 
    "Financial Engineer"
]
job_description = [
    "Control and Maintenance of systems",
    "Repair and installation of electrical systems",
    "Maintain and update the company's database",
    "Keep record and track of the company's financial and accounts state "
]

# Create your views here.
def job_list(request):
    
    list_of_jobs = "<h1>Engineering jobs available</h1> <ul>"
    for j in job_title:
        job_id = job_title.index(j)
        detail_url = reverse('jobs_detail', args=(job_id,))
        list_of_jobs += f"<li><a href = '{detail_url}'>{j}</a></li>"
    list_of_jobs += "</ul>"
    return HttpResponse(list_of_jobs)


# job detail page
def job_detail(request, id):
    print(type(id))
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("Not Found")
    # site = 'http://google.com'
    # return HttpResponse(f"Please <a href={site}>Get jobs here</a>")
    # return HttpResponse(f"<h1>Control Engineering job {id} details</h1> ")   