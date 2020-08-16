from django import forms

class SimulateRFIDCodeForm(forms.Form):
    rfid_code = forms.CharField(label="RFID")