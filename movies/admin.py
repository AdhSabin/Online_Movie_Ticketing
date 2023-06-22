from django.contrib import admin
from .models import User, City, Theatre, Hall, Movie, Show, Ticket, NextMovies
# Register your models here.

admin.site.register(User)
admin.site.register(City)
admin.site.register(Theatre)
admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Ticket)
# admin.site.register(Movies)
admin.site.register(NextMovies)

admin.site.site_header="Online Movie Ticketing"
admin.site.index_title="Online Movie Ticketing Administration"
admin.site.site_title="Online Movie Ticketing Admin"