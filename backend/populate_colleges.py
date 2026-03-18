import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "college_review_backend.settings")
django.setup()

from colleges.models import College, Course, Facility

def populate_data():
    # Clear existing data
    College.objects.all().delete()

    colleges_data = [
        {
            "name": "Indian Institute of Technology, Bombay",
            "location": "Mumbai, Maharashtra",
            "description": "IIT Bombay is one of the premier engineering institutes in India, known for its excellence in technology and research.",
            "established_year": 1958,
            "website": "https://www.iitb.ac.in",
            "courses": [
                {"name": "B.Tech Computer Science", "fee": 200000, "duration": "4 Years"},
                {"name": "B.Tech Electrical Engineering", "fee": 200000, "duration": "4 Years"},
                {"name": "M.Tech Data Science", "fee": 150000, "duration": "2 Years"}
            ],
            "facilities": [
                {"name": "Central Library", "icon": "Library"},
                {"name": "Sports Complex", "icon": "Activity"},
                {"name": "Computer Labs", "icon": "Monitor"}
            ]
        },
        {
            "name": "Delhi University",
            "location": "New Delhi, Delhi",
            "description": "The University of Delhi is a premier university of the country with a venerable legacy and international acclaim for highest academic standards.",
            "established_year": 1922,
            "website": "http://www.du.ac.in",
            "courses": [
                {"name": "B.A. (Hons) Economics", "fee": 15000, "duration": "3 Years"},
                {"name": "B.Com (Hons)", "fee": 18000, "duration": "3 Years"},
                {"name": "M.Sc Physics", "fee": 20000, "duration": "2 Years"}
            ],
            "facilities": [
                {"name": "Hostels", "icon": "Home"},
                {"name": "Auditorium", "icon": "Mic"},
                {"name": "Cafeteria", "icon": "Coffee"}
            ]
        },
        {
            "name": "Birla Institute of Technology and Science, Pilani",
            "location": "Pilani, Rajasthan",
            "description": "BITS Pilani is a deemed university and a premier institute for higher education and research in engineering and sciences.",
            "established_year": 1964,
            "website": "https://www.bits-pilani.ac.in",
            "courses": [
                {"name": "B.E. Computer Science", "fee": 450000, "duration": "4 Years"},
                {"name": "B.E. Electronics", "fee": 450000, "duration": "4 Years"},
                {"name": "MBA", "fee": 500000, "duration": "2 Years"}
            ],
            "facilities": [
                {"name": "Innovation Lab", "icon": "Zap"},
                {"name": "Swimming Pool", "icon": "Droplet"},
                {"name": "Smart Classrooms", "icon": "ScreenAttributes"}
            ]
        }
    ]

    for data in colleges_data:
        college = College.objects.create(
            name=data["name"],
            location=data["location"],
            description=data["description"],
            established_year=data["established_year"],
            website=data["website"]
        )
        print(f"Created college: {college.name}")

        for course_data in data["courses"]:
            Course.objects.create(
                college=college,
                **course_data
            )
        
        for facility_data in data["facilities"]:
            Facility.objects.create(
                college=college,
                **facility_data
            )

    print("Data population complete!")

if __name__ == "__main__":
    populate_data()
