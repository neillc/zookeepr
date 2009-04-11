import datetime

class Registration(object):
    def __init__(self,
                 over18=None,
                 nick=None,
                 shell=None,
                 editor=None,
                 editortext=None,
                 distro=None,
                 distrotext=None,
                 silly_description=None,
                 keyid=None,
                 planetfeed=None,
                 voucher_code=None,
                 diet=None,
                 special=None,
                 opendaydrag=None,
                 partner_email=None,
                 checkin=None,
                 checkout=None,
                 lasignup=None,
                 announcesignup=None,
                 delegatesignup=None,
                 prevlca=None,
                 miniconf=None,
                 ):
        self.over18 = over18
        self.nick = nick
        self.shell = shell
        self.editor = editor
        self.distro = distro
        self.silly_description = silly_description
        self.keyid = keyid
        self.planetfeed = planetfeed
        self.voucher_code = voucher_code
        self.diet = diet
        self.special = special
        self.opendaydrag = opendaydrag
        self.partner_email = partner_email
        self.checkin = checkin
        self.checkout = checkout
        self.lasignup = lasignup
        self.announcesignup = announcesignup
        self.delegatesignup = delegatesignup
        self.prevlca = prevlca
        self.miniconf = miniconf

    def __repr__(self):
        return '<Registration id=%r person_id=%r>' % (self.id, self.person_id)


class RegistrationProduct(object):
    def __init__(self, qty=0):
        self.qty = qty

    def __repr__(self):
        return '<RegistrationProduct registration_id=%r product_id=%r qty=%r>' % (self.registration_id, self.product_id, self.qty)

class RegoNote(object):
    def __init__(self, note=None):
        self.note = note

    def __repr__(self):
        return '<RegoNote note=%r>' % (self.note)

class Volunteer(object):
    def __init__(self, areas=None, other=None, accepted=None):
        self.areas = areas
        self.other = other
        self.accepted = accepted

    def __repr__(self):
        return '<Volunteer id=%r person_id=%r>' % (self.id, self.person_id)
