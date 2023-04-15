from django.contrib.admin import AdminSite
from django.contrib import admin

from reviews.models import (Book, Publisher, Contributor, BookContributor,Review)

def initialled_name(obj):
    """ obj.first_names='Jerome David' , obj.last_names='Salinger'
    => 'Salinger, JD' """
    initials = ''.join([name[0] for name in \
                        obj.first_names.split(' ')])
    return f"{obj.last_names}, {initials}"

class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name,)

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
admin_site.register(Contributor, ContributorAdmin)
admin_site.register(BookContributor)
admin_site.register(Review)
