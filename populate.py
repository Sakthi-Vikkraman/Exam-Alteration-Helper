import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exam_invigilator.settings')
django.setup()

from schedule.models import faculty, room, exam, conduct, student, adminlogin, constraints, tt, feed, head
# Create exam
exam1 = exam.objects.create(id=23, exam_date='2023-07-01', exam_time='9:00 AM', semester='3-1', dept='cse', subject='Math')
exam2 = exam.objects.create(id=24, exam_date='2023-07-02', exam_time='10:00 AM', semester='3-1', dept='it', subject='Physics')
# ... create more exam instances

# Create conduct
conduct1 = conduct.objects.create(fna1=faculty1, fna2='Some Faculty', ex=exam1, room=room)
# ... create more conduct instances

# Create student
student1 = student.objects.create(rollno='2023001', student_name='John Smith', stu_email='john@example.com', stu_dept='cse', year=3)
student2 = student.objects.create(rollno='2023002', student_name='Jane Doe', stu_email='jane@example.com', stu_dept='it', year=2)
# ... create more student instances

# Create adminlogin
adminlogin1 = adminlogin.objects.create(username='admin', password='password123')
# ... create more adminlogin instances

# Create constraints
constraints1 = constraints.objects.create(cname='Constraint 1', cdate='2023-07-01')
constraints2 = constraints.objects.create(cname='Constraint 2', cdate='2023-07-02')
# ... create more constraints instances

# Create tt
tt1 = tt.objects.create(Section='A', Branch='cse')
tt2 = tt.objects.create(Section='B', Branch='it')
# ... create more tt instances

# Create feed
feed1 = feed.objects.create(name='John Doe', email='john@example.com', feedback='Some feedback')
feed2 = feed.objects.create(name='Jane Smith', email='jane@example.com', feedback='Another feedback')
# ... create more feed instances

# Create head
head1 = head.objects.create(heading='EXAM TIMETABLE')
# ... create more head instances
