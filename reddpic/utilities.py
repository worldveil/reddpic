def splitcommas(option, opt, value, parser):
	setattr(parser.values, option.dest, value.split(','))