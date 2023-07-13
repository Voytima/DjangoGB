from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creation date')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Last change date')
    deleted = models.BooleanField(default=False, verbose_name='Deleted')

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class News(BaseModel):
    title = models.CharField(max_length=255, verbose_name='News header')
    preamble = models.CharField(max_length=1000, verbose_name='Introduction')
    body = models.TextField(verbose_name='Content')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Markdown option')

    def __str__(self):
        return f'#{self.pk} {self.title}'
    
    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Many news'
    
    
class Course(BaseModel):
    name = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name='As markdown', default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Cost', default=0)
    cover = models.CharField(max_length=25, default='no_image.svg', verbose_name='Cover')

    def __str__(self) -> str:
        return f'{self.pk} {self.name}'
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name='Lesson number')
    title = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    description_as_markdown = models.BooleanField(verbose_name='As markdown', default=False)

    def __str__(self) -> str:
        return f'{self.course.name} | {self.num} | {self.title}'
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
        ordering = ('course', 'num')


class CourseTeachers(BaseModel):
    course = models.ManyToManyField(Course)
    name_first = models.CharField(max_length=128, verbose_name='Name')
    name_last = models.CharField(max_length=128, verbose_name='Surname')
    day_birth = models.DateField(verbose_name='Birth date')
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return '{0:0>3} {1} {2}'.format(self.pk, self.name_last, self.name_first)
    
