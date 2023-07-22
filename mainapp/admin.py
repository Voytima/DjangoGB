from django.contrib import admin
from mainapp import models as mainapp_models
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _

from rangefilter.filter import DateRangeFilter

# Register your models here.


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'title', 'preamble']
    search_fields = ['title__icontains', 'preamble__icontains', 'body__icontains']
    list_filter = (('created_at', DateRangeFilter), 'created_at')


@admin.register(mainapp_models.Courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost']
    list_per_page = 4


@admin.register(mainapp_models.CourseTeachers)
class CourseTeachersAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'get_courses']
    list_select_related = True

    def get_courses(self, obj):
        return ", ".join((i.name for i in obj.courses.all()))
    
    get_courses.short_description = _("Courses")


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_course_name', 'num', 'title', 'created_at', 'deleted']
    list_editable = ['deleted']
    ordering = ['-course__name', 'num']
    list_filter = ['course', 'deleted', 'created_at']
    actions = ['mark_deleted', 'mark_active']
    list_per_page = 8

    def get_course_name(self, obj):
        return obj.course.name
    
    get_course_name.short_description = _('Course')


    def mark_deleted(self, request, queryset: QuerySet):
        queryset.update(deleted=True)

    mark_deleted.short_description = _('Mark course deleted')

    def mark_active(self, request, queryset: QuerySet):
        queryset.update(deleted=False)

    mark_active.short_description = _('Mark course ative')