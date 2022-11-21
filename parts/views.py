from django.shortcuts import render, redirect
from django.views import View
from users.models import User
from .models import ProductDetail, GalleryImage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ContactUsForm
from users.models import Cart
from django.contrib import messages
from base.messages import Message

class Home(View):

    def get(self, request):
        return render(request, 'index.html')


class ContactForm(View):

    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 Message.CONTACT_US)
            return render(request, 'contact.html')
        return render(request, 'contact.html')
        
        


class AboutUs(View):

    def get(self, request):
        return render(request, 'about.html')
    

class Base(View):

    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.filter(email=request.user).first()
            return render(request, 'base.html',{'user': user})
        return render(request, 'base.html')


class Parts(View):

    def get(self, request):
        product_data = ProductDetail.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(product_data, 3)
        try:
            part_data = paginator.page(page)
        except PageNotAnInteger:
            part_data = paginator.page(1)
        except EmptyPage:
            part_data = paginator.page(paginator.num_pages)
        return render(request, 'parts.html',{"product_data": part_data})
    
    def post(self, request):
        name = request.POST.get('search_data', None)
        if name:
            product_data = ProductDetail.objects.filter(vin=name)
            return render(request, 'parts.html', 
                          {"product_data": product_data})
        product_data = ProductDetail.objects.all()
        return render(request,'parts.html', {"product_data": product_data})


class PartDetail(View):

    def get(self, request, pk):
        product_data = ProductDetail.objects.filter(id=pk).first()
        return render(request, 'detail.html', {"product_data": product_data})


class AddPart(View):

    def get(self, request):
        return render(request, 'add_parts.html')

    def post(self, request):
        name = request.POST.get('name',None)
        price = request.POST.get('price',None)
        images_data = request.FILES.get('images',None)
        vin = request.POST.get('vin',None)
        info = request.POST.get('info',None)
        gallery_image = request.FILES.getlist('gallery_image',None)
        prod = ProductDetail.objects.create(
            name=name,
            price=price,
            vin=vin,
            info=info
        )
        if gallery_image:
            for image in gallery_image:
                img = GalleryImage.objects.create(images=image)
                prod.gallery_image.add(img)
                prod.save()
        if images_data:
            prod.image = images_data
            prod.save()
        return redirect('parts')



class AddToCart(View):

    def get(self, request, pk):
        if request.user.is_authenticated:
            product_detail = ProductDetail.objects.filter(id=pk).first()
            cart_data = Cart.objects.filter(user=request.user).first()
            if cart_data:
                cart_data.product.add(product_detail)
            else:
               cart_data = Cart.objects.create(user=request.user)
               cart_data.product.add(product_detail)
            return render(request, 'add_to_cart.html', 
                          {"cart_data": cart_data})
        else:
            return redirect('login')

    def post(self, request, pk):
        cart_id = request.POST.get('purchase_item',None)
        cart = Cart.objects.filter(id=cart_id).first()
        if cart:
            cart.is_puchase = True
            cart.save()
        messages.add_message(request, messages.SUCCESS,
                                 Message.ITEM_PUCHASE)
        cart.product.clear()
        cart.is_puchase = False
        cart.save()
        return redirect('parts')
