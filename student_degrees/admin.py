from django.contrib import admin
from .models import Student, Degree

class DegreeInline(admin.StackedInline):
    model = Degree
    extra = 0

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']
    list_filter = ['name']
    inlines = [DegreeInline]
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(['Name', 'Email'])

        for student in queryset:
            writer.writerow([student.name, student.email])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=students.csv'
        return response

    export_as_csv.short_description = "Export selected students as CSV"

class DegreeAdmin(admin.ModelAdmin):
    list_display = ('name', 'student', 'grade')
    list_filter = ['name', 'student']
    search_fields = ['name', 'student__name']
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(['Name', 'Student', 'Grade'])

        for degree in queryset:
            writer.writerow([degree.name, degree.student.name, degree.grade])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=degrees.csv'
        return response

    export_as_csv.short_description = "Export selected degrees as CSV"

admin.site.register(Student, StudentAdmin)
admin.site.register(Degree, DegreeAdmin)