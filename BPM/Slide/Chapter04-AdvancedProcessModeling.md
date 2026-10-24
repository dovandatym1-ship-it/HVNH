# Chapter04-AdvancedProcessModeling

- **Tài liệu nguồn:** `Chapter04-AdvancedProcessModeling.pdf`
- **Định dạng gốc:** `.pdf`
- **Công cụ chuyển đổi:** MarkItDown (Microsoft Open Source)
- **Thời gian chuyển đổi:** 2026-10-13 19:48:22

---

Chapter 4: Advanced Process Modeling

Contents

1. More on Rework and Repetition

2. Handling Events

3. Handling Exceptions

4. Processes and Business Rules

5. Recap

Process Modeling in the BPM Lifecycle

Examples for BPM lifecycle and process mining

!"#$%&&'
)(%,-).)$I-)#,

50%01"4"%.&6I)8"(("(

!"#$%"&'$($)%

!"*"+),&-.I0."12

34,+"4"%.&
-.I0."12

50%01"&;$(<

9)I"&6I)8"(("(

6I)8:I"
50."I$0+(

6I)8:I"
6I)=:8.(

50I<".
6I)=:8.(

!"+$*"I&
6I)=:8.(

50%01"&
9:(.)4"I&
-"I*$8"

!"#$%&&'I"$4)-%$-5"%

50%01"&6"I()%%"+

50%01"
3%#)I40.$)%&

50%01"&7((".(

-:,,)I.&6I)8"(("(

35h

30h

B

15h

A

3m

5m

5m

D

10m

30m

E

2h

10m

C

15m

1.5h

10min

?#,.#"1I,$%'I,('
2%".#"1I,$%'
),&)34-&

!"#$%&&'
()&$#*%"+

6&7)&'2"#$%&&
1#(%0

A

B

C

D

E

!"#$%&&
1#,)-#"),3

=>%$5-I<0%'
2"#$%&&
1#(%0

!"#$%&&
I,I0+&)&

8,&)34-&'#,
9%I:,%&&%&'I,('
-4%)"')12I$-

!"#$%&&
)120%1%,-I-)#,

;#7<%'2"#$%&&'
1#(%0

!"#$%&&
"%(%&)3,

More on rework and repetition

XOR-join: entry
point

XOR-split: exit point

Structured
cycle (SESE
fragment)

SESE = Single Entry Single Exit fragment, i.e. a fragment delimited by a single entry
node and a single exit node (there are no other incoming arcs into the fragment or
outgoing arcs from the fragment)

Block-structured repetition: Loop Activity

BPMN also provides the loop activity construct to allow the repetition of a task or
sub-process

!"#$
%&&'

()*+',&-.##
%&&'

Example: block-structured repetition

Completion
condition

;F+EI&-#*A.F*#&E*&%AA"./#:

U**EPF&
'EFE*+#"E%I&
4FR6E"7

2F/#*+EP%+#&
'EFE*+#"E%I&
4FR6E"7

1EF%IE*#&
'EFE*+#"E%I&
-#*A.F*#

'EFE*+#"E%I&
4FR6E"7
"#9#E/#:

'EFE*+#"E%I&
4FR6E"7
<EFEIE=#:

!"#A%"#&
'EFE*+#"E%I&
-#*A.F*#

-#/E#M&
'EFE*+#"E%I&
-#*A.F*#

4FR6E"7
EF/#*+EP%+#:

-#*A.F*#
"#/E#M#:

Must have a
decision activity

Arbitrary Cycles

Arbitrary = unstructured, i.e. it can have multiple entry and exit nodes (non-SESE).

entry point

D

!
#

"

!

entry point

exit point

"
A

exit point

#
B

C

6

Exercise 4.1

§ Identify the entry and exit points that delimit the unstructured cycles in the process

model shown below. What are the repetition blocks?

Exercise 4.1

§ Identify the entry and exit points that delimit the unstructured cycles in the

process model shown below. What are the repetition blocks?

§ Model the business process shown below using a loop activity.

9

Example: multi-instance activity

Procurement

In procurement, typically a quote is to be obtained from all preferred
suppliers (assumption: five preferred suppliers exist). After all quotes
are received, they are evaluated and the best quote is selected. A
corresponding purchase order is then placed.

10

Solution: without multi-instance activity

Procurement

!"#ABCDE)*#+D
,-*.D/)001B+-DO

!"#ABCDE)*#+D
,-*.D/)001B+-DP

;;;

!"#ABCDE)*#+D
,-*.D/)001B+-DQ

/+1+7#D"+8#D
9)*#+

:1A7+D:!

;;;

!"#ABCDE)*#+D
,-*.D/)001B+-D5

!"#ABCDE)*#+D
,-*.D/)001B+-DS

11

Parallel repetition: multi-instance activity

Provides a mechanism to indicate that an activity is executed multiple
times concurrently

!"#$%&'()$*(+I-
.*)/

!"#$%&'()$*(+I-
."/&M12+I))

Useful when the same activity needs to be executed for multiple entities
or data items, such as:

§ Request quotes from multiple suppliers
§ Check the availability for each line item in an order separately
§ Send and gather questionnaires from multiple witnesses in the context of an

insurance claim

12

Solution: with multi-instance activity

Procurement

0+1&"-$O&(*PP#Q"1

cardinality

///

.'%-Q5&S*+%"

!"#"$%&'"(%&
F*+%"

,#-$"&,.

///

13

Further example: multi-instance activity

Motor insurance claim lodgement

After a car accident, a statement is sought from the witnesses that were
present, in order to lodge the insurance claim. As soon as the first two
statements are received, the claim can be lodged to the insurance
company without waiting for the other statements.

Solution: multi-instance activity

Motor insurance claim lodgement

Data collection
denotes a set of data
objects of the same type
(determines cardinality of
multi-instance activity)

Multi-instance pool
denotes multiple
participants of the
same type

Completion
condition indicates
minimum number of
instances required to
complete
(≤ cardinality)

15

Our order-to-cash example…
now with pools, messages and MI markers

Exercise 4.2

Model the following process fragment.

After a car accident, a statement is sought from two witnesses out of
the five that were present in order to lodge the insurance claim. As
soon as the first two statements are received, the claim can be
lodged with the insurance company without waiting for the other
statements

Uncontrolled Repetition: Ad-hoc sub-process

Contains activities to be executed in arbitrary order and number of times

May define order of sub-set of activities by sequence flow

Can be used in an early version of a process diagram
when the order of execution is still unknown

Completion
condition

!"#$%&'%%&()*+&I-K$-/-0

Example: Ad-hoc sub-process

18

19

Exercise 4.3: Army recruitment

Model the following process snippet.

A typical army selection process starts by shortlisting all candidates’ applications.
Those shortlisted are then called to sit the following tests: drug and alcohol, eye,
color vision, hearing, blood, urine, weight, fingerprinting and doctor examination.
The color vision can only be done after the eye test, while the doctor examination
can only be done after color vision, hearing, blood, urine and weight have been
tested. Moreover, it may be required for some candidates to repeat some of
these tests multiple times in order to get a correct assessment, e.g. the blood
test may need be repeated if the candidate has taken too much sugar in the
previous 24 hours. The candidates that pass all tests are asked to sit a mental
exam and a physical exam, followed by an interview. Only those that also pass
these two exams and perform well in the interview can be recruited in the army.

20

How do we model this scenario?

PO handling

A Purchase Order (PO) handling process starts when a PO is received.
The PO is first registered. If the current date is not a working day, the
process waits until the following working day before proceeding.
Otherwise, an availability check is performed and a PO response is sent
back to the customer.

21

Events handling

In BPMN, events model something instantaneous happening during the execution
of a process

They affect the process flow:

§ Start
§ Intermediate
§ End

22

BPMN event types

Start

Intermediate

End

!"#$%&'E)*&"#E!"#$%&'()*+")I()"($"&$+)($'*"-.")I*"
/0-'*++"&+"'0*()*%"1+)(0)2"-0"'-3/4*)*%"1*$%25"
6&)I-T)"+/*'&.8&$9")I*"'(T+*".-0"'0*()&-$:'-3/4*)&-$

Catching

+#I-#E.&//IM&E)*&"#"!"#$%&'()*+")I()"($"&$+)($'*"
-.")I*"/0-'*++"&+"'0*()*%"6I*$"("3*++(9*"&+"
-&1&2*&'

)"'E.&//IM&E)*&"#"!"#$%&'()*+")I()"($"&$+)($'*"-."
)I*"/0-'*++"&+"'-3/4*)*%"6I*$"("3*++(9*"&+"/&"#

3"#&-4&'2I#&E.&//IM&E)*&"#"!"#$%&'()*+")I()"($"
*;*$)"&+"*</*')*%")-"-''T0"%T0&$9")I*"/0-'*++=">I*"
*;*$)"&+")0&99*0*%"6I*$"("3*++(9*"&+"-&1&2*&'E-0"
/&"#

Example: message events

.:E,A
SF?"%"#A,+@
A":%

P4R2.:E,A

!"#A"%C#

>:,2+882'EFC0#

.L0*12P4R2'EFC02S7+"8+9"8"AJ

.:E,A2.+80%F+,
;0*0"70F

'EF"*"+,J

Start event
(receive)

.L0*12.:E,A2
.+80%F+,

;0YE0#A2
="AA"%C#2!"#A

.:E,A2.+80%F+,
.L+%C02;0YE0#A

.L+%C02P4R2
=*L0FE80#

="AA"%C#2!"#A
;0*0"70F

A0+,8J2
=*L0FE80
=0%A

Intermediate
catching event
(receive)

;0#:8702P4R2
'EFC02
S7+"8+9"8"AJ

End event
(send)

Comparison with sending/receiving tasks

!"#$%&'
('&'%#')

!"#$%&'
('")

!"#$%&'
('")

!"#$%&'
('&'%#')

=

=

=

≠

!"#"$%"&
$'%($#"

!"#$%&#'(&)"

!"#$%&#'(&)"

!"#"$%"&
$'%($#"

So, when to use what?

Use message events only when the corresponding activity would simply send or
receive a message and do nothing else

Exercise 4.4
Is there any other activity in the loan assessment model below that can be replaced
by a message event?

Temporal events

Start

Intermediate

End

!"#$"%&'E)$%*+)I"!"!#$%&'(F*+!FI(F!($!&$+F($'*!-.!FI*!
/0-'*++!&+!'0*(F*%!(F!'*0F(&$!%(F*1+23F&4*1+25!*6T6!+F(0F!
/0-'*++!(F!8/4!*9*0:!;0&%(:

-I")$E).'#")%&'E)$%*+)I"!"!<0&TT*0*%!(F!'*0F(&$!%(F*1+23
F&4*1+25!-0!(.F*0!(!F&4*!&$F*09(=!I(+!*=(/+*%!+&$'*!FI*!
4-4*$F!FI*!*9*$F!&+!!*$(>=*%"!1%*=(:2

Example: temporal events

In a small claims tribunal, callovers occur once a month to set down the
matter for the upcoming trials. The process for setting up a callover starts
three weeks prior to the callover day, with the preparation of the callover
list containing information such as contact details of the involved parties
and estimated hearing date. One week prior to the callover, the involved
parties are notified of the callover date. Finally, on the callover day, the
callover material is prepared and the callover is held.

!"#$%"#C
'%(()*#"C(H,-

4)5-%'-C
$%"-H#,

.C/##0,C$"H)"C
-)C'%(()*#"C
1%2
Start
event

PC/##0C$"H)"C
-)C'%(()*#"C
1%2

Intermediate
catching event

'%(()*#"C1%2

Intermediate
catching event

!"#$%"#C
'%(()*#"C
6%-#"H%(

7)(1
'%(()*#"

'%(()*#"
8#(1

Coming back to our scenario…

PO handling
A Purchase Order (PO) handling process starts when a PO is received.
The PO is first registered. If the current date is not a working day, the
process waits until the following working day before proceeding.
Otherwise, an availability check is performed and a PO response is sent
back to the customer.

."/C(0N'OAP#(-4R

0""O"P-S
7N8A-4R

!"#A%C"'()*

0""O-4R

97"+O(
:,4A84;A8ACR

<"P-()*(
!"%=NP%"

)*
!"+"A,"-

)*
>?8>A88"-

Multiple start events

The first start event that occurs will trigger an instance of the process

EN'PO.4"/.O
PO+O$RO6

7**"*'8O..-MO
PO+O$RO6

9*$6-&
-%#O*/""/

E*"+O..'EN'
PO.4"/.O

!"#$%&'
EF*+,-.$/M'
N%%$+O*

31

Exercise 4.4: Internet Service Provider

Model the billing process of an Internet Service Provider (ISP).

The ISP sends an invoice by email to the customer on the first working day of
each month (Day 1). On Day 7, the customer has the full outstanding amount
automatically debited from its bank account. If an automatic transaction fails for
any reason, the customer is notified on Day 8. On Day 9, the transaction that
failed on Day 7 is re-attempted. If it fails again, on Day 10 a late fee is charged to
the customer’s bank account. At this stage, the automatic payment is no longer
attempted. On Day 14, the Internet service is suspended until payment is
received. If the payment is still outstanding on Day 30, the account is closed and
a disconnection fee is applied. A debt-recovery procedure is then started.

32

Racing events: Event-based decision

With the XOR-split gateway, a branch is chosen based on conditions
that evaluate over available data

à The choice can be made immediately after the token arrives from

the incoming flow

Sometimes, the choice must be delayed until an event happens

à The choice is based on a “race” among events

Two types of XOR split:

data-driven
XOR-split

event-driven
XOR split

Example: Event-based decision

33

Exercise 4.6: Stock replenishment

Model the following process.

A restaurant chain submits a purchase order (PO) to replenish its warehouses
every Thursday. The restaurant chain’s procurement system expects to receive
either a “PO Response” or an error message. However, it may also happen that
no response is received at all due to system errors or due to delays in handling
the PO on the supplier’s side. If no response is received by Friday afternoon or if
an error message is received, a purchasing officer at the restaurant chain’s
headquarters should be notified. Otherwise, the PO Response is processed
normally.

Matching choices in different business parties
Lead-to-Quote

Matching a
data-driven
choice at Client

19

What’s wrong with this collaboration diagram?
Auction creation

Solution
Auction creation

Exercise 4.7

Fix the following
collaboration diagram.

Recap: message and timer events

Start

Intermediate

End

Catching

Throwing

Untyped: indicate start point,
state changes or final states.

Message: Receiving and
sending messages.

Timer: Cyclic timer events,
points in time, time spans or
timeouts.

40

Process abortion

Exceptions are events that deviate a process from its “normal” course

The simplest form of exception is to notify that there is an exception
(negative outcome)

This can be done via the Terminate end event: it forces the whole
process to abort (“wipes off” all tokens left behind, if any)

41

Example 1: terminate event

Signal the negative outcome…

42

Example 2: terminate event

Abort the process by removing all tokens…

Exercise 4.8

Revise the examples presented so far by using the terminate event
appropriately.

44

Exception handling

Handling exceptions often involves stopping a sub-process and performing a special activity

Types of exceptions for an activity (task/sub-process):

Internal: something goes wrong inside an activity, whose execution must
thus be interrupted. Handled with the Error event

External: something goes wrong outside the process, and the execution
of the current activity must be interrupted. Handled with the Message
event

Timeout: an activity takes too long and must be interrupted. Handled
with the Timer event

All these events are catching intermediate events. They stop the enclosing activity and
start an exception handling routine.

45

Internal exception: error event

Start

Intermediate

End

!""#"$!%&'E!"!#$%&'()*+!($!*II-I.!)/*!!*$%"#0*I+&-$!1*$*I()*+!($!
*II-I!*0*$)!2/&3*!)/*!!'()'/&$1!&$)*I4*%&()*"#0*I+&-$!'-$+54*+!&)!
2/*$!())('/*%!)-!)/*!6-5$%(I7!-8!($!(')&0&)7

Must be attached to
the activity’s boundary

46

Example: internal exception

PO handling

Consider again our “PO Handling process” example with the following extension:
if an item is not available, any processing related to the PO must be stopped.
Thereafter, the client needs to be notified that the PO cannot be further
processed.

!"#A%C'()

0""O"P-S
7N8A-4R

OCP.'4R/S,#H'A"7

."/C(0N'OAP#(-4R
4CCSC#A8
9R%,A"7

*CH,-.C/'()
!"#A%C"'()*

0""O-4R

4CCSA"7

97"+O(
:,4A84;A8ACR

:9C0S'
;N",%"<,%,.7

<"P-()*(
!"%=NP%"

=C#A'()'
*C->R#-C

)*
()
*C0C,NCA
!"+"A,"-

()
*CH,-.C/CA

)*
>?8>A88"-

*C->R#-C
-C#.

()
?@%?,%%CA

47

Solution: internal exception

PO handling

Throwing and catching
error events must have
the same label

!"#A%C'()

!"#A%C'()

4CCSC#A8
4CCSC#A8
9R%,A"7
9R%IA"7

OCP.'4R/SI#H'A"7

OCP.'4R/S,#H'A"7

A.CB-'#R.'
"N"I%"<%C

*CH,-.C/'()
*CHI-.C/'()

()
()
*C0C,NCA
*C0CINCA

()
()
*CH,-.C/CA
*CHI-.C/CA

4CCSA"7

4CCSA"7

:9C0S'
:9C0S'
;N",%"<,%,.7
;N"I%"<I%I.7

=C#A'()'
*C->R#-C

=C#A'()'
*C->R#-C

A.CB-
"N"I%"<%C

*C->R#-C
*C->R#-C
-C#.
-C#.

()
?@%?,%%CA

()
?@%?I%%CA

!"#$%&'("&
)*)+I)-I#

.("+/+0)"+('
%#'"

Must catch an error
event thrown from
within the same
activity

48

One more example: internal exception

Extend the claim handling process shown below as follows:

After checking the insurance policy, a possible outcome is that the
insurance is invalid. In this case, any processing is cancelled and a letter
is sent to the customer. In the case of a complex claim, this implies that
the damage checking is cancelled if it has not yet been completed.

0*.1)#C(2C
$(.1)#PC
$)-*.

!"#$%CD()*$+

!)-00*4+C!)-*.

!)-*.
2#$#*5#6

$(.1)#PC
$)-*.

!"#$%C,-.-/#

!)-*.
$"#$%#6

49

Solution: internal exception

!"#$%CD()*+I($#
!"#$%CD()*+I($#

0*.1)#C(2C
$(.1)#PC
$)-*.

)D24/#C.+C
)D24/#C.+C
$.24/#5C$/ID2
$.24/#5C$/ID2

!"#$%CD()*$+

!"#$%C-./D$0
!"#$%C-./D$0

-./D$0CD)C
D(6I/D7

D(6I/D7
4./D$0

6I/D7
4./D$0

!/ID2
!/ID2
(##7)C:#
(##8)C:#
$/I))D8D#7
$/I))D6D#8

$(.1)#PC
$)-*.

$.24/#5C
$.24/#5C
!"#$%C,-.-/#
$/ID2
$/ID2

!"#$%C1I2IP#
!"#$%C1I2IP#

!)-*.
$"#$%#4

9()*+I($#
7()*+I($#
$"#$%#7
$"#$%#8

!/ID2
!/ID2
$"#$%#7
$"#$%#8

!/I))D80C!/ID2
!)-00*5+C!)-*.
!/I))D60C!/ID2

!)-*.
!/ID2
!/ID2
2#$#*6#4
+#$#D6#7
+#$#D9#8

."/$0C'$*
$N2P/$4

!"#$%C'
()*#"+,-

(/P$+
-,5,0#,4

50

Example: external exception

PO handling

A PO change request may be received anytime after the PO is registered.
This request includes a change in quantity or line items. When such a
request is received, any processing related to the PO must be stopped.
The PO change request is then registered. Thereafter, the process
proceeds as it would do after a normal PO is registered. Further, if the
customer sends a PO cancelation request after the PO registration, the
PO processing must be stopped and the cancelation request must be
handled.

."/C(0N'OAP#(-4R

0""O"P-S
7N8A-4R

!"#A%C"'()*

0""O-4R

97"+O(
:,4A84;A8ACR

<"P-()*(
!"%=NP%"

)*
!"+"A,"-

)*
>?8>A88"-

Solution: external exception

PO handling

!"#A%C'()

0""O"P-S
7N8A-4R

OCP.'4R/S,#H'A"7

."/C(0N'OAP#(-4R
4CCSC#A8
9R%,A"7

*CH,-.C/'()
!"#A%C"'()*

0""O-4R

4CCSA"7

97"+O(
:,4A84;A8ACR

:9C0S'
;N",%"<,%,.7

<"P-()*(
!"%=NP%"

=C#A'()'
*C->R#-C

()
)*
*C0C,NCA
!"+"A,"-

()
*CH,-.C/CA

)*
>?8>A88"-

*C->R#-C
-C#.

()
?@%?,%%CA

!"#$%C'()
*)+),-).

!"#$%C'()
*('(H,(-

/)(,01)*#!"#
$%C'()

.%C-)(#!"
$%C'()%/H0C

!"
'%C'()(-

8

Exercise 4.9

Model the following routine for accessing an Internet bank service.

The routine for logging into an Internet bank account starts once the credentials entered from

the user have been retrieved. First, the username is validated. If the username is not valid, the
routine is interrupted and the invalid username is logged. If the username is valid, the number
of password trials is set to zero. Then, the password is validated. If this is not valid, the
counter for the number of trials is incremented and if lower than three, the user is asked to
enter the password again, this time together with a CAPTCHA test to increase the security
level. If the number of failed attempts reaches three times, the routine is interrupted and the
account is frozen. Moreover, the username and password validation may be interrupted
should the validation server not be available. Similarly, the server to test the CAPTCHA may
not be available at the time of log in. In these cases, the procedure is interrupted after
notifying the user to try again later. At any time during the log in routine, the customer may
close the web page, resulting in the interruption of the routine.

Exercise 4.10: activity timeout

Order-to-transportation quote

Once a wholesale order has been confirmed, the supplier transmits this order to
the carrier for the preparation of the transportation quote. In order to prepare the
quote, the carrier needs to compute the route plan (including all track points that
need to be traversed during the travel) and estimate the trailer usage.

By contract, wholesale orders have to be dispatched within four days from the
receipt of the order. This implies that transportation quotes have to be prepared
within 48 hours from the receipt of the order to remain within the terms of the
contract.

Solution: activity timeout
Order-to-transportation quote

55

Example: Non-interrupting boundary events

PO handling

!"#A%C'()

OCP.'4R/SI#H'A"7

4CCSC#A8
9R%IA"7

4CCSA"7

:9C0S'
;N"I%"<I%I.7

*CHI-.C/'()

()
*C0CINCA

()
*CHI-.C/CA

!"#$%C'()
*)+),-).

!"#$%C'()
*('(H,(-

/)(,01)*#!"#
$%C'()

.%C-)(#!"
$%C'()%/H0C

A.CB-'#R.'
"N"I%"<%C

A.CB-
"N"I%"<%C

!"#$%&'("&
)*)+I)-I#

=C#A'()'
*C->R#-C

*C->R#-C
-C#.

()
?@%?I%%CA

!"
'%C'()(-

.("+/+0)"+('
%#'"

The customer may send a request for address change after the PO registration. When such
a request is received, it is just registered, without further action.

56

Non-interrupting boundary events

Sometimes we may need to trigger an activity in parallel to the normal
flow, i.e. without interrupting the normal flow.

This can be achieved by using non-interrupting boundary events

Must be attached to
the activity’s boundary

57

Solution: non-interrupting boundary events

PO handling

!"#A%C'()

OCP.'4R/SI#H'A"7

4CCSC#A8
9R%IA"7

4CCSA"7

:9C0S'
;N"I%"<I%I.7

*CHI-.C/'()

()
*C0CINCA

()
*CHI-.C/CA

!"#$%C'()
*)+),-).

!"#$%C'()
*('(H,(-

/)(,01)*#!"#
$%C'()

.%C-)(#!"
$%C'()%/H0C

=C#A'()'
*C->R#-C

*C->R#-C
-C#.

()
?@%?I%%CA

A.CB-'#R.'
"N"I%"<%C

A.CB-
"N"I%"<%C

!"#$%&'("&
)*)+I)-I#

!"
'%C'()(-

.("+/+0)"+('
%#'"

.##-C**
(/A01C
-C(C23C#

!"#A%C'
()*%+,C-'
A##-C**

4)*%+,C-
A##-C**
)"#A%C#

Exercise 4.11
Consider the process for assessing loan applications below.

Exercise 4.11

Extend this process as follows.

An applicant who has decided not to combine the loan with a home insurance
plan may change its mind any time before the eligibility assessment has been
completed. If a request for adding an insurance plan is received during this
period, the loan provider will simply update the loan application with this request.

60

Complex Exceptions

PO handling

[…] Further, if the customer sends a PO cancelation request after the
[…] Further, if the customer sends a PO cancelation request after the
PO registration, the PO processing must be stopped and the change
PO registration, the request is first assessed. Based on the progress of
request needs to be handled.
the order handling (e.g. if items have already been fetched from
external warehouses) a penalty is determined and communicated to
the customer. The customer has 48 hours to accept the penalty and go
on with the cancelation or to stop the cancelation and continue with the
order handling.

Complex Exceptions: Signal event

• To send or receive a signal for synchronization purposes
• A signal is broadcasted without any specific target. Thus it can be

caught multiple times

• Signals are different than messages which are routed to a specific

target

Start

Intermediate

End

Catching

Throwing

Can be attached to the
activity’s boundary

Solution: non-interrupting event + signal event

PO handling

!"#A%C'()

*CHI-.C/'()

()
*C0CINCA

()
*CHI-.C/CA

OCP.'4R/SI#H'A"7

4CCSC#A8
9R%IA"7

4CCSA"7

:9C0S'
;N"I%"<I%I.7

A.CB-'#R.'
"N"I%"<%C

A.CB-
"N"I%"<%C

=C#A'()'
*C->R#-C

*C->R#-C
-C#.

()
?@%?I%%CA

!"#$%CD()
!"#$%C'()
*(D(+,(-
*('(H,(-

-.
H/'0C
1#)1C*CO

.%C-)(#!"
$%C'()%/H0C
!"#$%C'
(C)#*H,

P#)O*C'-.'
!"
1#)1C*#H4/)
'%C'()(-

.(/(*0+C(
D%CD()%/+NC
O(C%)/P

4N/+RP
O(C%)/P
/N#D67/N0(*

!"#$%&'("&
)*)+I)-I#

.##-C**
Broadcasts a signal to all
(/A01C
catching signal events
-C(C23C#
bearing same label
.("+/+0)"+('
%#'"

!"#A%C'
()*%+,C-'
A##-C**

-.
1#)1C*CO

8(96(7/
/N#7/NO
*(D(+,(-

!"
/N#=(
D%CD()(-

4)*%+,C-
A##-C**
)"#A%C#

8(96(7/
/N#DNC/+C6(
*(D(+,(-

!"
CN/
D%CD()(-

:;#<N6*7

Event sub-process

To handle events that may not refer to a particular task/ sub-process within a
process

!"#$%&'E)*+,-.#//

!"#$%
&'E)*+,-#..
/

§ Placed into a process or subprocess

§ Is activated when its start event is triggered
§ It may or may not interrupt the parent process or sub-process, depending on

the type of its start event:

§ Non-Interrupting:

§ Interrupting:

Example: event sub-process

PO handling

!"#A%C'()
!"#A%C'()

*CHI-.C/'()
*CHI-.C/'()

()
()
*C0CINCA
*C0CINCA

()
()
*CHI-.C/CA
*CHI-.C/CA

OCP.'4R/SI#H'A"7
OCP.'4R/SI#H'A"7

4CCSC#A8
4CCSC#A8
9R%IA"7
9R%IA"7

4CCSA"7
4CCSA"7

:9C0S'
:9C0S'
;N"I%"<I%I.7
;N"I%"<I%I.7

A.CB-'#R.'
A.CB-'#R.'
"N"I%"<%C
"N"I%"<%C

A.CB-
A.CB-
"N"I%"<%C
"N"I%"<%C

=C#A'()'
=C#A'()'
*C->R#-C
*C->R#-C

*C->R#-C
*C->R#-C
-C#.
-C#.

()
()
?@%?I%%CA
?@%?I%%CA

.$%('C)!")
*$%#C'$/,0%

!")*$%#C'
HC#C,-C(

!"
#$%#C'C(

!"#$%
&'"()*)+I)-I#

.'"+/+0)"+'&
%#&"Only receptive of events
occurring during the
execution of the enclosing
sub-process

-,*)A'+
."#A%C'(+
)**('##

!"#A%C'(
)**('##+",*)A'*

/**('##
.0)12'+('.'34'*

!"#$%C'()
*)+),-).

/)(,01)*#!"#
$%C'()

0I%-./
!"
(%&'()*

!"#$%&'()*
HI%-./-

!"
$%&'()*
)/1/(O/-

Exercise 4.12

Model the following business process for reimbursing expenses.

After an expense report is received from an employee, the employee is notified of
the receipt of the report. Next, a new account must be created if the employee
does not already have one. The report is then reviewed for automatic approval.
Amounts under EUR 1,000 are automatically approved while amounts equal to or
over EUR 1,000 require manual approval. In case of rejection, the employee must
receive a rejection notice by email. In case of approval, the reimbursement is
deposited directly to the employee's bank account and an approval notice is sent
to the employee via email, with the details of the money transfer. At any time
during the review, the employee can send a request for amount rectification. In
that case the rectification is registered and the report needs to be reviewed again.
Moreover, if the report is not handled within 30 days, the process is stopped and
the employee receives a cancelation notice email so that he can resubmit the
expense report from scratch.

66

Example: activity compensation

PO handling

After a PO has been registered, checked, and a response has been sent
back, a payment sub-process and a fulfilment sub-process are started.
During these two sub-processes, a PO cancellation may be received
from the customer. In this case, both sub-processes are stopped, and
their effects are reverted (e.g. reimbursement and/or goods return may
need to occur).

67

Activity compensation

§ Rollback of completed process activities

§ May be used as part of an exception handling procedure

§ Triggered by throwing Compensate event

§ Compensation Handler (a catching Compensate event + a Compensate activity)

performs the rollback

!"#$%C'()*"C
+(C,-%.

68

Solution: activity compensation
PO handling

!"#$%#C'(FCG'HCG,

The compensate
activity can be a
sub-process

;'(F#.CG,

G,C0.8.%9.F

:

Only one compensate
activity must be linked
from a catching
compensate event

G'H-.(/

7'(8.#CG,

0.1
%-O"P4.-.(/

!"#$%##-.(/

G,
$"#$%##.F
'(FC<'%F

7'(8.#CG,

R66F4CP./"P(

G,C7'(8.#CP.8.%9.F

7'(8.#CG,

69

Compensate event

• Indicates that the enclosing activity must be compensated
• The “throwing intermediate” and the “end” version generate the

compensation event

• The “intermediate catching” version triggers the compensation when

attached to the boundary of an activity

Start

Intermediate

End

Catching

Throwing

!"#$%C'E)%*+,%C)
!"#$%&'()%*
+%&%,()%-).%-!"#$%&'()/"&-%0%&)-1./2%-).%-
0%,'/"&-!"&'3#%'-/)

Must be attached to the
activity’s boundary

Exercise 4.13

Modify the model created in Exercise 4.13 as follows.

If the report is not handled within 30 days, the process is stopped, the
employee receives a cancelation notice email and must resubmit the
expense report. However, if the reimbursement for the employee’s expenses
had already been made, a money recall needs to be made, to get the money
back from the employee, before sending the cancelation notice email.

71

Recap: Events

Start

Intermediate

End

g
n
i
h
c
t
a
C

y
r
a
d
n
u
o
B

g
n
i
t
p
u
r
r
e
t
n

I

-
n
o
N
y
r
a
d
n
u
o
B

g
n
i
t
p
u
r
r
e
t
n

I

g
n
i
w
o
r
h
T

Untyped: indicate start point,
state changes or final states.

Message: Receiving and
sending messages.

Timer: Cyclic timer events,
points in time, time spans or
timeouts.

Signal: Signalling across
different processes. A signal
can be caught multiple times.

Error: Catching or throwing
named errors.

Compensate: Handling or
triggering compensation.

Terminate: Triggering the
immediate termination of a
process.

72

Processes and Business Rules

• Business rules implement organizational policies or practices

• Example: in an online shop platinum customers have a 20% discount

for purchases over EUR 250.

• In BPMN, business rules can be captured via:

• Decision activities

• Conditions on outgoing arcs of (X)OR-split

• Conditional events

Example: conditional event

Replenishment order

73

Exercise 4.14

Model the following business process snippet.

In a stock exchange, stock price variations are continuously monitored
during the day. A day starts when the opening bell rings and concludes when
the closing bell rings. Between the two bells, every time the stock price
changes by more than 10%, the entity of the change is first determined.
Next, if the change is high, a “high stock price” alert is sent, otherwise a “low
stock price” alert is sent.

Recap

1. Structured loops can be modelled with loop activities, but

arbitrary cycles cannot

2. Multi-instance activities model activities that need to be

executed multiple times without a-priori knowledge of their
number

3. Multi-instantiation extends to business objects and resources
4.
Intermediate events can either be catching or throwing
5. Message events capture message exchange at the start,

during and at the end of a process

6. Timer events capture temporal events (absolute or periodic)

Recap (cont‘ed)

7. Exceptions can be technology or business based, and either internal,

external or activity timeouts

8. The simplest way to handle exceptions is via process abortion using

terminate events

9. Boundary error events capture internal extensions

10. Boundary message events capture external extensions

11. Boundary timer events capture activity timeouts

12. Signal events broadcast multiple messages and can be used to

capture complex exceptions

13. Compensation events are required to revert the effects of completed

activities

14. Conditional events are one way of capturing business rules

