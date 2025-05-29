from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    employees = models.ManyToManyField(Employee, through='Assignment', related_name='projects')

    def __str__(self):
        return self.name

class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    assigned_date = models.DateField()

    def __str__(self):
        return f"{self.employee} - {self.project} ({self.role})"

    class Meta:
        unique_together = ('employee', 'project')
