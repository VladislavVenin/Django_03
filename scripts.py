from datacenter.models import Mark
from datacenter.models import Chastisement
from datacenter.models import Lesson
from datacenter.models import Commendation
import random


def fix_marks(schoolkid):
    child = schoolkid
    Mark.objects.filter(schoolkid=child, points__in=[2, 3]).update(points=5)


def remove_chastisements(schoolkid):
    child = schoolkid
    chastisements = Chastisement.objects.filter(schoolkid=child)
    chastisements.delete()


def create_commendation(schoolkid):
    child = schoolkid
    year = schoolkid.year_of_study
    letter = schoolkid.group_letter
    lessons = Lesson.objects.filter(year_of_study=year, group_letter=letter)
    lesson = random.choice(lessons)
    date = lesson.date
    subject = lesson.subject
    teacher = lesson.teacher
    Commendation.objects.create(text="Хвалю!", created=date, schoolkid=child, subject=subject, teacher=teacher)