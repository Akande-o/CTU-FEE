# Pride and Prejudice by Jane Austen
text1 = '''It is a truth universally acknowledged, that a single man in
        possession of a good fortune, must be in want of a wife.
        However little known the feelings or views of such a man may be
        on his first entering a neighbourhood, this truth is so well
        fixed in the minds of the surrounding families, that he is
        considered the rightful property of some one or other of their
        daughters.'''
 
# Sense and Sensibility by Jane Austen
text2 = '''The family of Dashwood had long been settled in Sussex.  Their estate
was large, and their residence was at Norland Park, in the centre of
their property, where, for many generations, they had lived in so
respectable a manner as to engage the general good opinion of their
surrounding acquaintance.  The late owner of this estate was a single
man, who lived to a very advanced age, and who for many years of his
life, had a constant companion and housekeeper in his sister.  But her
death, which happened ten years before his own, produced a great
alteration in his home; for to supply her loss, he invited and received
into his house the family of his nephew Mr. Henry Dashwood, the legal
inheritor of the Norland estate, and the person to whom he intended to
bequeath it.  In the society of his nephew and niece, and their
children, the old Gentleman's days were comfortably spent.  His
attachment to them all increased.  The constant attention of Mr. and
Mrs. Henry Dashwood to his wishes, which proceeded not merely from
interest, but from goodness of heart, gave him every degree of solid
comfort which his age could receive; and the cheerfulness of the
children added a relish to his existence.'''
text1 = text1.replace(".", "")
text1 = text1.replace(",", "")
text1_words = text1.split()
text1_set = set(text1_words)

text2 = text2.replace(".", "")
text2 = text2.replace(",", "")
text2_words = text2.split()
text2_set = set(text2_words)

common_words = text1_set & text2_set
print(common_words)

only_in_pap = text1_set - text2_set
print("#############")
print(only_in_pap)
