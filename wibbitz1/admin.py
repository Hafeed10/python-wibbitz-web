# admin.py

from django.contrib import admin
from .models import Customer, Subscribe, Featured, Videoblog, Testimonial, Marketing, Business, Videoresources, Contact, Img, Latest_customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']  

admin.site.register(Customer, CustomerAdmin)

admin.site.register(Subscribe)

class FeaturedAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'icon_logo', 'description', 'title', 'testimonial_description', 'testimonial_author', 'author_description', 'testimonial_logo']

admin.site.register(Featured, FeaturedAdmin)

class VideoblogAdmin(admin.ModelAdmin):
    list_display =['id', 'image', 'title', 'logo']

admin.site.register(Videoblog, VideoblogAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'description', 'name', 'company_name', 'is_featured', 'p_designation']  # Update 'designation_old' to 'designation'

admin.site.register(Testimonial, TestimonialAdmin)

class MarketingAdmin(admin.ModelAdmin):
    list_display =['id', 'image', 'title', 'description', 'a_description']

admin.site.register(Marketing, MarketingAdmin)

class BusinessAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'description', 'image']

admin.site.register(Business, BusinessAdmin)

class VideoresourcesAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'heding', 'description', 'spana']

admin.site.register(Videoresources, VideoresourcesAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'email','first_name', 'last_name',' company',' company_size', 'industry', ' job_role', 'connrty', 'user']
    
admin.site.register(Contact)

admin.site.register(Img)

admin.site.register( Latest_customer)





 