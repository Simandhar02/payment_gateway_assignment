class URL(object):
    def __init__(self, url, resource, name=None):
        self.url = url
        self.resource = resource
        self.name = name


def app_prefix(url_obj, prefix):
    url_obj.url = prefix + url_obj.url
    return url_obj


URL_LIST_API_V1 = (
    URL("/payment/process/", "resources.process_payment.PaymentProcess", name="payment_process"),
    URL("/cheap/gateway/", "resources.payment_gateways.CheapPayment", name="cheap_payment_gateway"),
    URL("/expensive/gateway/", "resources.payment_gateways.ExpensivePayment", name="expensive_payment_gateway"),
    URL("/premium/gateway/", "resources.payment_gateways.PremiumPayment", name="premium_payment_gateway")
)

URL_LIST = [app_prefix(url_obj, "api/v1") for url_obj in URL_LIST_API_V1]
