class AnalyzerResult:

    severity = None
    result = None

    def __init__(self, severity=None,summary=None,detail=None,recommendation=None,other_results=None):
        self._collector_result = None
        self._analyzer = None
        # self.analysis = None

        self.severity = severity

        self.results = {}

        if summary is not None:
            self.results['summary'] = summary
        if detail is not None:
            self.results['detail'] = detail
        if recommendation is not None:
            self.results['recommendation'] = recommendation

        if other_results is not None:
            for key in other_results:
                self.results[key] = other_results[key]

    @property
    def collector_result(self):
        """
        Collector result
        """
        return self._collector_result

    @collector_result.setter
    def collector_result(self,collector_result):
        """
        Set collector result
        """
        self._collector_result = collector_result

    @property
    def analyzer(self):
        """
        Analyzer
        """
        return self._analyzer

    @analyzer.setter
    def analyzer(self,analyzer):
        """
        Set analyzer
        """
        self._analyzer = analyzer

    def format(self, data=None):
        format_attributes = {}
        if self.collector_result is not None:
            for k in self.collector_result.__dict__:
                format_attributes['collector_result_' + k] = self.collector_result.__dict__[k]
        if data is not None:
            for k in data:
                format_attributes[k] = data[k]

        for field in self.results:
            if self.results[field] is not None:
                self.results[field] = self.results[field].format(**format_attributes)
        

    # @property
    # def analysis(self):
    #     """
    #     Analyzer results
    #     """
    #     return self._analysis

    # @analyzer.setter
    # def analysis(self,analyzer):
    #     """
    #     Set analyzer
    #     """
    #     self._analysis = analyzer

