<%init>
#if c.signed_in_person and c.signed_in_person.email_address == 'erikd@mega-nerd.com':
#	logo = '/sicktux.png'
#else:
logo = '/mel8-logo.png'
</%init>
<h1><% h.link_to(h.image_tag(logo, alt="linux.conf.au 2008"), url=h.url('home')) %></h1>
<h2>
January 2008<br />
Melbourne, Australia
</h2>

