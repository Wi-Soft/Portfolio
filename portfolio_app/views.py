from django.shortcuts import render
from .models import Project

def index(request):
    experiences = [
        {
            "period": "Jan 2025 - To-Date",
            "title": "Casual Worker",
            "company": "Central Bank of Kenya",
            "responsibilities": [
                "General cleaning",
                "Cash handling support",
                "Handle confidential documents",
                "Data Entry & Records Management",
                "Scanning cheques and managing clearing documents",
                "Team Collaboration",
                "Operational Support",
                "Filing & Organization",
                "Confidentiality and Integrity",
                "Adherence to Procedures"
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
            "icon": "📘",
            "period": "2021 October - 2021 Novermber",
            "institution": "Infotect college",
            "degree": "Computer Packages",
            "details": "Pass"
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
            "period": "Jan 2025 - To-Date",
            "title": "Casual Worker",
            "company": "Central Bank of Kenya",
            "responsibilities": [
                "General cleaning",
                "Cash handling support",
                "Handle confidential documents",
                "Data Entry & Records Management",
                "Scanning cheques and managing clearing documents",
                "Team Collaboration",
                "Operational Support",
                "Filing & Organization",
                "Confidentiality and Integrity",
                "Adherence to Procedures"
            ]
        },
        {
            "period": "Oct 2022 - March 2023",
            "title": "Annotation",
            "company": "Remotask",
            "responsibilities": [
                "Task Execution & Performance",
                "Training and Onboarding Responsibilities",
                "Quality Assurance",
                "Legal & Professional Obligations"
            ]
        }
    ]

    context = {
        "experiences": experiences
    }

    return render(request, "experience.html", context)


