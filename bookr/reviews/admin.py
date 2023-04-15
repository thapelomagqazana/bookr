from django.contrib.admin import AdminSite
from django.contrib import admin

from reviews.models import (Book, Publisher, Contributor, BookContributor,Review)

class BookrAdminSite(AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Book Administration'
    index_title = 'Bookr site admin'

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')

admin_site = BookrAdminSite(name='bookr')

# Register your models here.
admin_site.register(Book, BookAdmin)
admin_site.register(Publisher)
admin_site.register(Contributor)
admin_site.register(BookContributor)
admin_site.register(Review)
