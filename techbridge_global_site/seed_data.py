from core.models import CompanySettings, ServiceCategory, ServiceItem, ProcessStep, FAQ, Testimonial

CompanySettings.objects.get_or_create(
    company_name='TechBridge Global Limited',
    defaults={
        'tagline':'Technology, talent and relocation support for international companies.',
        'email':'info@techbridgeglobal.com',
        'phone':'+852 0000 0000',
        'address':'Hong Kong',
        'hero_title':'Building the bridge between technology, talent and global mobility',
        'hero_subtitle':'We provide software development, IT consulting, high-tech recruitment and relocation coordination for companies expanding internationally.',
    }
)

data = [
    ('💻','Software Development','Custom digital solutions for companies that need reliable technology delivery.',[
        ('Custom Software Development','Design and development of tailored software solutions for business operations.'),
        ('Web & Application Development','Modern websites, portals, dashboards and business applications.'),
        ('Automation & Integrations','Workflow automation, API integrations and system connectivity.'),
    ]),
    ('🧠','IT Consulting','Technical advisory and digital project support for international clients.',[
        ('IT Project Support','Planning, coordination and support for technology projects.'),
        ('Digital Business Solutions','Analysis and implementation of practical digital tools.'),
        ('Technical Documentation','Preparation of specifications, process flows and user guidance.'),
    ]),
    ('👥','Tech Recruitment','Recruitment support focused on IT, software and high-tech professionals.',[
        ('Candidate Sourcing','Search and identification of suitable technology candidates.'),
        ('Pre-screening & Shortlisting','CV review, initial checks, interview coordination and shortlists.'),
        ('Skills Assessment Coordination','Coordination of technical checks and client interview processes.'),
    ]),
    ('✈️','Relocation & Travel Coordination','Employee relocation and travel support connected with recruitment and onboarding.',[
        ('Travel Arrangements','Coordination of flights, accommodation and journey details.'),
        ('Relocation Support','Administrative and logistic coordination for employee relocation.'),
        ('Third-party Provider Coordination','Working with external suppliers and adding a transparent service fee.'),
    ]),
]
for order, (icon, title, desc, items) in enumerate(data, start=1):
    cat, _ = ServiceCategory.objects.get_or_create(title=title, defaults={'icon':icon,'description':desc,'order':order})
    for idx, (ititle, idesc) in enumerate(items, start=1):
        ServiceItem.objects.get_or_create(category=cat, title=ititle, defaults={'description':idesc,'order':idx})

steps = [
    (1,'Understand the requirement','We review the client request, business need, role profile, technology scope or relocation requirement.'),
    (2,'Prepare service plan','We define the service scope, timeline, responsibilities, supplier involvement and fee structure.'),
    (3,'Deliver and coordinate','We manage development tasks, recruitment pipeline, interviews, travel or relocation coordination.'),
    (4,'Report and improve','We provide clear updates, keep records and improve the process based on client feedback.'),
]
for number,title,desc in steps:
    ProcessStep.objects.get_or_create(number=number, defaults={'title':title,'description':desc})

faqs = [
    ('Do you work internationally?','Yes. The company is designed for B2B clients requiring international technology, recruitment and coordination services.'),
    ('Can services be customized?','Yes. Services can be provided separately or as a combined package depending on the client requirement.'),
    ('Do you work with third-party providers?','Yes. Where required, we coordinate external suppliers and charge a transparent service or management fee.'),
]
for i,(q,a) in enumerate(faqs, start=1):
    FAQ.objects.get_or_create(question=q, defaults={'answer':a,'order':i})

Testimonial.objects.get_or_create(client_name='International Client', defaults={'client_role':'B2B Technology Partner','quote':'TechBridge Global provides a clear and professional structure for technology delivery and international talent support.'})
print('Seed data created successfully.')
