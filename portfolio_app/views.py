from django.shortcuts import render
from .models import Project

def index(request):
    experiences = [
        {
            "period": "2024",
            "title": "Django Portfolio Development",
            "company": "Personal Projects",
            "responsibilities": [
                "Built modular Django applications with reusable templates.",
                "Implemented Django model relationships and database migrations.",
                "Created RESTful APIs using Django REST Framework.",
                "Configured static and media assets for production-ready deployment."
            ]
        },
        {
            "period": "2023",
            "title": "Web Application Support",
            "company": "Freelance / Contract",
            "responsibilities": [
                "Designed and deployed Django sites using Git and CI/CD.",
                "Enhanced application performance and user interface workflows.",
                "Maintained Django settings, URL routing, and template rendering.",
                "Implemented test-driven development for reliable feature rollouts."
            ]
        }
    ]

    education_data = [
        {
            "icon": "🎓",
            "period": "Jan 2023 - Dec 2025",
            "institution": "eMobilis Technology Training Institute",
            "degree": "Diploma in Information Technology",
            "details": "Distinction"
        },
        {
            "icon": "🏫",
            "period": "2017 - 2021",
            "institution": "Motiret Secondary School",
            "degree": "Kenya Certificate of Secondary Education (KCSE)",
            "details": "Grade: C (plain)"
        },
        {
            "icon": "📘",
            "period": "2007 - 2016",
            "institution": "Chesegem Primary School",
            "degree": "Kenya Certificate of Primary Education (KCPE)",
            "details": "Score: 291 out of 500"
        }
    ]

    context = {
        "experiences": experiences,
        "education": education_data
    }

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')


def header(request):   
    return render(request, 'header.html')


def project(request):
    return render(request, 'project.html')
def skills(request):
    return render(request, 'skills.html')

def base(request):
    return render(request, 'base.html')




def education(request):
    education_data = [
        {
            "icon": "🎓",
            "period": "Jan 2023 - Dec 2025",
            "institution": "eMobilis Technology Training Institute",
            "degree": "Diploma in Information Technology",
            "details": "Distinction"
        },
        {
            "icon": "🏫",
            "period": "2017 - 2021",
            "institution": "Motiret Secondary School",
            "degree": "Kenya Certificate of Secondary Education (KCSE)",
            "details": "Grade: C (plain)"
        },
        {
            "icon": "📘",
            "period": "2007 - 2016",
            "institution": "Chesegem Primary School",
            "degree": "Kenya Certificate of Primary Education (KCPE)",
            "details": "Score: 291 out of 500"
        }
    ]

    context = {
        "education": education_data
    }

    return render(request, "education.html", context)



def experience(request):
    experiences = [
        {
            "period": "2024" - "Present",
            "title": "Django Portfolio Development",
            "company": "Personal Projects",
            "responsibilities": [
                "Built modular Django applications with reusable templates.",
                "Implemented Django model relationships and database migrations.",
                "Created RESTful APIs using Django REST Framework.",
                "Configured static and media assets for production-ready deployment."
            ]
        },
        {
            "period": "2023",
            "title": "Web Application Support",
            "company": "Freelance / Contract",
            "responsibilities": [
                "Designed and deployed Django sites using Git and CI/CD.",
                "Enhanced application performance and user interface workflows.",
                "Maintained Django settings, URL routing, and template rendering.",
                "Implemented test-driven development for reliable feature rollouts."
            ]
        }
    ]

    context = {
        "experiences": experiences
    }

    return render(request, "experience.html", context)