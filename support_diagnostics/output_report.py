import fcntl
import termios
import struct

import support_diagnostics

class Report(support_diagnostics.Output):
    rows = None
    columns = None

    def static_init():
        pad = "0" * 8
        s = fcntl.ioctl(1, termios.TIOCGWINSZ, pad)
        sz = struct.unpack('hhhh', s)
        Report.rows = sz[0]
        Report.columns = sz[1]
        # print("rows: {} columns: {}, xpixels: {}, ypixels: {}". format(*sz))

    def generate(self, analyser_results):
        for analyzer in analyser_results:
            print(support_diagnostics.Colors.format("{header}{padding}".format(header=analyzer.heading,padding=" " * (Report.columns - len(analyzer.heading))), support_diagnostics.Colors.WHITE_FOREGROUND, support_diagnostics.Colors.BLUE_BACKGROUND))
            if analyser_results[analyzer] is not None:
                for analyzer_result in analyser_results[analyzer]:
                    # !!! filter severity
                    if analyzer_result.severity is not None:
                        print(support_diagnostics.Colors.format(analyzer_result.severity.name, analyzer_result.severity.foreground_color, analyzer_result.severity.background_color))

                    if 'summary' in analyzer_result.results:
                        print(support_diagnostics.Colors.format("{header:<16}{result}".format(header="Summary", result=analyzer_result.results['summary'])))

                    if 'detail' in analyzer_result.results:
                        print(support_diagnostics.Colors.format("{header:<16}{result}".format(header="Detail", result=analyzer_result.results['detail'])))

                    if 'recommendation' in analyzer_result.results:
                        print(support_diagnostics.Colors.format("{header:<16}{result}".format(header="Recommendation", result=analyzer_result.results['recommendation'])))

                    # All other results.
                    for key in analyzer_result.results:
                        if key != 'summary' and key != 'detail' and key != 'recommendation':
                            print(support_diagnostics.Colors.format("{header:<16}{result}".format(header=key.capitalize(), result=analyzer_result.results[key])))

                    # print()
        print()
        
if Report.rows is None:
    Report.static_init()