import scrapy


class PytorchSpider(scrapy.Spider):
    name = "pytorchSpider"


    start_urls = ["https://github.com/pytorch/pytorch/issues/" + str(issue_num) for issue_num in range(67635, 89295)]

    def get_comments(self, response):
        """Finds the number of comments on a issue page

        Args:
            response (Object): The respnse received after request by scrapy

        Returns:
            int: number of comments
        """
        xpath_to_comments = 'div.timeline-comment-header'
        num_of_comments = len(response.css(xpath_to_comments).getall())
        return num_of_comments



    def get_labels(self, response):
        """returns labels assigned to the issue

        Args:
            response (Object): The respnse received after request by scrapy

        Returns:
            str: lables of the issue separated by comma
        """
        xpath_to_labels = 'div.js-issue-labels a span::text'
        labels_list = response.css(xpath_to_labels).getall()
        labels = ",".join(labels_list)
        return labels



    def get_assignees(self, response):
        """returns assignees of the issue

        Args:
            response (Object): The respnse received after request by scrapy

        Returns:
            str: username of assignees separated by comma
        """
        xpath_to_assignees = 'span.js-issue-assignees p span a.assignee span::text'
        assignees_list = response.css(xpath_to_assignees).getall()
        assignees = ",".join(assignees_list)
        return assignees

    
    def get_reviewers(self, response):
        """returns the reviewers of the issue

        Args:
            response (Object): The respnse received after request by scrapy

        Returns:
            str: username of reviewers separated by comma
        """
        xpath_to_reviewers = 'span p.d-flex  span a.assignee span::text'
        reviewers_list = response.css(xpath_to_reviewers).getall()
        reviewers = ','.join(reviewers_list)
        return reviewers

    
    def get_participants(self, response):
        """returns participants of the issue

        Args:
            response (Object): The respnse received after request by scrapy

        Returns:
            str: username of the participants separated by comma
        """
        xpath_to_participants = 'div.participation div a.participant-avatar::attr(href)'
        participants_list = [participant[1:] for participant in response.css(xpath_to_participants).getall()]
        participants = ','.join(participants_list)
        return participants


    def get_issue_status(self, response):
        """returns the status of the issue

        Args:
            response (Object): The respnse received after request by scrapy

        Returns:
            str: the issue status
        """
        xpath_to_issue_status = 'div.gh-header div.gh-header-meta div span::attr(title)'
        issue_status = response.css(xpath_to_issue_status).get().split()[1]
        return issue_status



    
    def get_description_code(self, response):
        """returns if the description contains code

        Args:
            response (Object): The respnse received after request by scrapy

        Returns:
            str: True if the description of the issue contains code
        """
        xpath_to_description_code = 'tbody tr td.comment-body  pre::text'
        description_code_exists = 1 if len(response.css(xpath_to_description_code).getall())>0 else 0
        return description_code_exists


    def parse(self, response):
        """using other modules processes the response and generates json objects containing the data extracted of response

        Args:
            response (Object): The respnse received after request by scrapy

        Yields:
            json: the data extracted of response
        """

        num_of_comments = self.get_comments(response)
        labels = self.get_labels(response)
        assignees = self.get_assignees(response)
        reviewers = self.get_reviewers(response)
        participants = self.get_participants(response)
        issue_status = self.get_issue_status(response)
        description_code_exists = self.get_description_code(response)

        yield {
            "issue_url" : {response.request.url},
            "num_of_comments" : {num_of_comments},
            "labels" : {labels},
            "assignees" : {assignees},
            "reviewers" : {reviewers},
            "participants" : {participants},
            "status" : {issue_status},
            "description_code_exists" : {description_code_exists}
        }