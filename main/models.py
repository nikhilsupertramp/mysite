from django.db import models

# Create your models here.:
class Interns(models.Model):
    intern_name=models.TextField()
    intern_job=models.TextField()
    intern_joined=models.DateTimeField("date joined")
      

    def __str__(self):
        return self.intern_name



class keyword(models.Model):
      keyword_author=models.CharField(max_length=20)
      keyword=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
       
      def __str__(self):
        return self.keyword

class sdg1(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword

class sdg2(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword

class sdg3(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword

class sdg4(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg5(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg6(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg7(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg8(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg9(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg10(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg11(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg12(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg13(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword

class sdg14(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg15(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg16(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
class sdg17(models.Model):
      keyword=models.CharField(max_length=20)
      keyword_author=models.CharField(max_length=20)
      date_added=models.DateTimeField(auto_now_add=True)
     
      def __str__(self):
        return self.keyword
