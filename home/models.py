from django.db import models



class City(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name

class District(models.Model):
    name = models.CharField(max_length=30)
   
    def __str__(self) -> str:
        return self.name


class Car_type(models.Model):
    name = models.CharField(max_length=30)

    
    def __str__(self) -> str:
        return self.name




class Car_category(models.Model):
    brand = models.CharField(max_length=40)
    type = models.ForeignKey(Car_type,on_delete=models.CASCADE)
    car_year = models.IntegerField(default=0)

    
    def __str__(self) -> str:
        return self.brand



class Driver(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    car_category = models.ForeignKey(Car_category,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name


# class Passager(models.Model):
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     phone = phonenumber.PhoneNumber()
#     district = models.ForeignKey(District,on_delete=models.CASCADE)

# class Location(models.Model):
#     x = models.IntegerField(default=0)
#     y = models.IntegerField(default=0)
#     district = models.ForeignKey(District,on_delete=models.CASCADE)



# class Speed(models.Model):
#     name = models.CharField(max_length=30)




# class Order(models.Model):
#     location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
#     speed = models.ForeignKey(Speed, on_delete=models.CASCADE)
#     description = models.CharField(max_length=200)
#     order_photo = models.ImageField()
#     avarage_price = models.IntegerField(default=0)
   