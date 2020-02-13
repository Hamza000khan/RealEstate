from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices


from django.contrib.auth.decorators import login_required
from django.utils import timezone


from .models import Listing


def create(request):
  if request.method == 'POST':
    if request.POST['title'] and request.POST['address'] and request.POST['city'] and request.POST['state'] and request.POST['zipcode'] and request.POST['description'] and request.POST['price'] and  request.POST['bedrooms'] and request.POST['bathrooms'] and request.POST['garage'] and request.POST['sqft'] and request.POST['lot_size']:
      listing = Listing()
      listing.title = request.POST['title']
      listing.address = request.POST['address']
      listing.city = request.POST['city']
      listing.state = request.POST['state']
      listing.zipcode = request.POST['zipcode']
      listing.description = request.POST['description']
      listing.price = request.POST['price']
      listing.bedrooms = request.POST['bedrooms']
      listing.bathrooms = request.POST['bathrooms']
      listing.garage = request.POST['garage']
      listing.sqft = request.POST['sqft']
      listing.lot_size = request.POST['lot_size']
      # listing.photo_main = request.FILES['photo_main']
      # listing.photo_1 = request.FILES['photo_1']
      # listing.photo_2 = request.FILES['photo_2']
      # listing.photo_3 = request.FILES['photo_3']
      # listing.photo_4 = request.FILES['photo_4']
      # listing.photo_5 = request.FILES['photo_5']
      # listing.photo_6 = request.FILES['photo_6']
      listing.list_date = timezone.datetime.now()
      listing.save()
      return redirect('/listings/')
    else:
      return render(request, 'listings/create.html', {'error': 'all fields are required'})
  else:
    return render(request, 'listings/create.html')



@login_required(login_url="/accounts/login")
def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }

  return render(request, 'listings/listings.html', context)

@login_required(login_url="/accounts/login")
def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)

@login_required(login_url="/accounts/login")
def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)