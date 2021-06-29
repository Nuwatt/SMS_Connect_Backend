from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class ResponseAnswerPagination(LimitOffsetPagination):
    def get_custom_paginated_response(self, data, response_cycle):

        info = OrderedDict([
            ('agent_id', response_cycle.agent_id),
            ('questionnaire_id', response_cycle.questionnaire_id),
        ])
        return Response(OrderedDict([
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('info', info),
            ('results', data)
        ]))
