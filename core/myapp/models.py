from django.db import models

class Image_Result(models.Model): 
    # django automatically adds the id = AutoField(primary_key=True) so need to add that.
    image = models.ImageField(upload_to="images/")
    predicted_digit = models.IntegerField()
    prediction_score = models.FloatField()

    def __str__(self):
        return f"{self.image} has digit {self.predicted_digit} with score {self.prediction_score}"

class Logs(models.Model):
    date = models.DateField()
    time = models.TimeField()
    level = models.CharField(max_length=20)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.message