# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Disciplines(models.Model):
    discipline_id = models.AutoField(blank=True, primary_key=True)
    discipline_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disciplines'


class Groups(models.Model):
    group_id = models.AutoField(blank=True, primary_key=True)
    group_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'

    def __str__(self):
        return self.group_name


class LessonTypes(models.Model):
    lesson_type_id = models.AutoField(blank=True, primary_key=True)
    lesson_type_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lesson_types'


class Lessons(models.Model):
    lesson_id = models.AutoField(blank=True, primary_key=True)
    group_num = models.ForeignKey(Groups, models.DO_NOTHING, db_column='group_num', blank=True, null=True)
    occupation = models.ForeignKey('Occupations', models.DO_NOTHING, db_column='occupation', blank=True, null=True)
    discipline = models.ForeignKey(Disciplines, models.DO_NOTHING, db_column='discipline', blank=True, null=True)
    teacher = models.ForeignKey('Teachers', models.DO_NOTHING, db_column='teacher', blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    call_num = models.ForeignKey('ScheduleCalls', models.DO_NOTHING, db_column='call_num', blank=True, null=True)
    week = models.IntegerField(blank=True, null=True)
    lesson_type = models.ForeignKey(LessonTypes, models.DO_NOTHING, db_column='lesson_type', blank=True, null=True)
    room = models.ForeignKey('Rooms', models.DO_NOTHING, db_column='room', blank=True, null=True)
    include = models.TextField(blank=True, null=True)
    exception = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lessons'


class Occupations(models.Model):
    occupation_id = models.AutoField(blank=True, primary_key=True)
    occupation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'occupations'


class Rooms(models.Model):
    room_id = models.AutoField(blank=True, primary_key=True)
    room_num = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rooms'


class ScheduleCalls(models.Model):
    call_id = models.AutoField(blank=True, primary_key=True)
    call_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedule_calls'


class Teachers(models.Model):
    teacher_id = models.AutoField(blank=True, primary_key=True)
    teacher_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teachers'
