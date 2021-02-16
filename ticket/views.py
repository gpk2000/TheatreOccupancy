from django.views.generic import TemplateView
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from .forms import TicketForm
from .models import Ticket

# Create your views here.
class OccupyView(TemplateView):
    template_name = 'occupy.html'

    
    def get(self, request):
        """
        creates a new form and sends it to the html template for input.
        """

        form = TicketForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        """
        Takes the input from the submit button and checks if the input
        is valid. 

        If the input is valid, then checks if you can allocate a seat
        to the person.

        If seat can be allocated add this user to database, else print
        respective error message.
        """

        form = TicketForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            seat = self.get_seat_num()

            if seat:
                newTicket = Ticket(name=name, seat_num=seat)
                newTicket.save()

                return HttpResponse("<h3>Success!! Your seat number is " + \
                                    str(newTicket.seat_num))
            else:
                return HttpResponse("<h3>Sorry 😟 Try again Later (Seats are completely Full)")



    def get_seat_num(self):
        """
        Checking if a seat is unoccupied by all the members in database.
        """

        for seat in range(1, settings.MAX_OCCUPANCY+1):
            cnt = 0
            for ticket in Ticket.objects.all():
                if ticket.seat_num != seat:
                    cnt += 1
            if cnt == len(Ticket.objects.all()):
                return seat
        return None
