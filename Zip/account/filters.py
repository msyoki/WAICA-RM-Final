
import django_filters
from account.models import UserActivityLog
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field


class UserActivityLogFilter(django_filters.FilterSet):
    COUNTRIES = (
    ('HQ', 'HQ'),  # Sierra Leone
    ('KE', 'KE'),  # Kenya
    ('ZW', 'ZW'),  # Zimbabwe
    ('NG', 'NG'),  # Nigeria
    ('TN', 'TN'),  # Tunisia
    ('GH', 'GH'),  # Ghana
    ('CIV', 'CIV'),  # Ivory Coast
    )

    # Activity_Choices= (
    #     ('login successful', 'login successful'),
    #     ('Failed login', 'Failed login'),
    # )
    # activity=django_filters.ChoiceFilter(label='Activity', 
    #     choices=Activity_Choices, 
    # )

    country=django_filters.ChoiceFilter(label='Country', 
        choices=COUNTRIES, 
    )
    class Meta:
        model = UserActivityLog
        fields=[
            'date',
            'country',
            
        ]
      