from django import forms

class TestForm(forms.Form):

    SOME_CHOICES= [
        ('value','Display Value'),
        ('value1','Display Value1'),
        ('value2','Display Value2'),
    ]

    INTS_CHOICES= [tuple([x,x]) for x in range(0,100)]

    YEARS= [x for x in range(1980,2031)]

    date_field= forms.DateField(initial="2020-20-5",widget=forms.SelectDateWidget(years=YEARS))
    text = forms.CharField(label="My text",min_length=7,widget=forms.Textarea) 
    radio_choices = forms.CharField(widget=forms.RadioSelect(choices=SOME_CHOICES)) 
    checkbox_choices = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=SOME_CHOICES)) 
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10,widget=forms.Select(choices=INTS_CHOICES))
    email = forms.EmailField()

    def clean_integer(self):
        integer= self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer