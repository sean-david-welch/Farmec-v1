from suppliers.models import Supplier
from spareparts.models import SupplierPage

def navbar_links(request):
    """Adds navbar links to the context"""
    suppliers = Supplier.objects.all()
    spareparts = SupplierPage.objects.all()
    return {'suppliers': suppliers, 'spareparts': spareparts}