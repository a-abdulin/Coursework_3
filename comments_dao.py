class CommentsDao:

    def __init__(self, post_id=0, commenter_name='', comment='', pk=0):
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk


    def __repr__(self):
        return f"\n({self.post_id},\n{self.commenter_name},\n{self.comment},\n{self.pk})\n"