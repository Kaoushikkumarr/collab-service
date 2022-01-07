"""Collaboration_Controller"""


class Collaborations:
    """This is a class for Collaborations Test."""

    def get_response_for_api(self):
        """ GET method for Collaboration."""
        coll_1 = "I'm from Collaboration"
        coll_2 = " Controller Class"
        result = coll_1 + coll_2
        return {
            'response': result
        }
