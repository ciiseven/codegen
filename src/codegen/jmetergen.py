from lxml import etree

def hashTree(root):
	hashTree = etree.SubElement(root, 'hashTree')
	return hashTree

def boolProp(r, n, v):
	e = etree.SubElement(r, "boolProp")
	e.set("name", n)
	e.text = v

def stringProp(r, n, v):
	e = etree.SubElement(r, "stringProp")
	e.set("name", n)
	e.text = v

def jmeterTestPlan():
	root = etree.Element("jmeterTestPlan", )
	root.set("version", "1.2")
	root.set("properties", "5.0")
	root.set("jmeter", "5.4.3")
	return root

def testPlan(root):
	testPlan = etree.SubElement(root, "TestPlan")
	testPlan.set("guiclass", "TestPlanGui")
	testPlan.set("testclass", "TestPlan")
	testPlan.set("testname", "Test Plan")
	testPlan.set("enabled", "true")

	boolProp(testPlan, "TestPlan.functional_mode", "false")
	boolProp(testPlan, "TestPlan.tearDown_on_shutdown", "true")
	boolProp(testPlan, "TestPlan.serialize_threadgroups", "true")
	stringProp(testPlan, "TestPlan.comments", "")
	stringProp(testPlan, "TestPlan.user_define_classpath", "")

	elementProp = etree.SubElement(testPlan, "elementProp")
	elementProp.set("name", "TestPlan.user_defined_variables")
	elementProp.set("elementType", "Arguments")
	elementProp.set("guiclass", "ArgumentsPanel")
	elementProp.set("testclass", "Arguments")
	elementProp.set("testname", "User Defined Variables")
	elementProp.set("enabled", "true")
	collectionProp = etree.SubElement(elementProp, "collectionProp")
	collectionProp.set("name", "Arguments.arguments")

def resultCollector(root):
	resultCollector = etree.SubElement(root, "ResultCollector")
	resultCollector.set("guiclass", "ViewResultsFullVisualizer")
	resultCollector.set("testclass", "ResultCollector")
	resultCollector.set("testname", "View Results Tree")
	resultCollector.set("enabled", "true")
	boolProp(resultCollector, "ResultCollector.error_logging", "false")
	objProp = etree.SubElement(resultCollector, "objProp")
	name = etree.SubElement(objProp, "name")
	name.text = "saveConfig"
	value = etree.SubElement(objProp, "value")
	value.set("class", "SampleSaveConfiguration")
	values = {"time": "true", "latency": "true", "timestamp": "true", "success": "true",
	"label": "true", "code": "true", "message": "true", "threadName": "true",
	"dataType": "true", "encoding": "false", "assertions": "true", "subresults": "true",
	"responseData": "false", "samplerData": "false", "xml": "false", "fieldNames": "true",
	"responseHeaders": "false", "requestHeaders": "false", "responseDataOnError": "false",
	"saveAssertionResultsFailureMessage": "true", "assertionsResultsToSave": "0",
	"bytes": "true", "sentBytes": "true", "url": "true", "threadCounts": "true",
	"idleTime": "true", "connectTime": "true", }
	for k, v in values.items():
		n = etree.SubElement(value, k)
		n.text = v

def headerManager(root):
	headerManager = etree.SubElement(root, 'HeaderManager')
	headerManager.set("guiclass", "HeaderPanel")
	headerManager.set("testclass", "HeaderManager")
	headerManager.set("testname", "HTTP Header Manager")
	headerManager.set("enabled", "true")

	collectionProp = etree.SubElement(headerManager, "collectionProp")
	collectionProp.set("name", "HeaderManager.headers")

	elementProp = etree.SubElement(collectionProp, "elementProp")
	elementProp.set("name", "")
	elementProp.set("elementType", "Header")

	stringProp(elementProp, "Header.name", "Content-Type")
	stringProp(elementProp, "Header.value", "application/json")

def threadGroup(root):
	threadGroup = etree.SubElement(root, "ThreadGroup")
	threadGroup.set("guiclass", "ThreadGroupGui")
	threadGroup.set("testclass", "ThreadGroup")
	threadGroup.set("testname", "Thread Group")
	threadGroup.set("enabled", "true")
	boolProp(threadGroup, "ThreadGroup.same_user_on_next_iteration", "true")
	boolProp(threadGroup, "ThreadGroup.scheduler", "false")

	stringProp(threadGroup, "ThreadGroup.delay", "")
	stringProp(threadGroup, "ThreadGroup.duration", "")
	stringProp(threadGroup, "ThreadGroup.num_threads", "1")
	stringProp(threadGroup, "ThreadGroup.on_sample_error", "continue")
	stringProp(threadGroup, "ThreadGroup.ramp_time", "1")

	elementProp = etree.SubElement(threadGroup, "elementProp")
	elementProp.set("name", "ThreadGroup.main_controller" )
	elementProp.set("elementType", "LoopController")
	elementProp.set("guiclass", "LoopControlPanel")
	elementProp.set("testclass", "LoopController")
	elementProp.set("testname", "Loop Controller")
	elementProp.set("enabled", "true")
	boolProp(elementProp, "LoopController.continue_forever", "false")
	stringProp(elementProp, "LoopController.loops", "1")

def httpSamplerProxy(root, name, url, data="{}"):
	httpSamplerProxy = etree.SubElement(root, "HTTPSamplerProxy")
	httpSamplerProxy.set("guiclass", "HttpTestSampleGui")
	httpSamplerProxy.set("testclass", "HTTPSamplerProxy")
	httpSamplerProxy.set("testname", name)
	httpSamplerProxy.set("enabled", "true")
	boolProp(httpSamplerProxy, "HTTPSampler.auto_redirects", "false")
	boolProp(httpSamplerProxy, "HTTPSampler.DO_MULTIPART_POST", "false")
	boolProp(httpSamplerProxy, "HTTPSampler.follow_redirects", "true")
	boolProp(httpSamplerProxy, "HTTPSampler.postBodyRaw", "true")
	boolProp(httpSamplerProxy, "HTTPSampler.use_keepalive", "true")
	stringProp(httpSamplerProxy, "HTTPSampler.connect_timeout", "")
	stringProp(httpSamplerProxy, "HTTPSampler.contentEncoding", "utf-8")
	stringProp(httpSamplerProxy, "HTTPSampler.domain", "")
	stringProp(httpSamplerProxy, "HTTPSampler.embedded_url_re", "")
	stringProp(httpSamplerProxy, "HTTPSampler.method", "POST")
	stringProp(httpSamplerProxy, "HTTPSampler.path", url)
	stringProp(httpSamplerProxy, "HTTPSampler.port", "")
	stringProp(httpSamplerProxy, "HTTPSampler.protocol", "")
	stringProp(httpSamplerProxy, "HTTPSampler.response_timeout", "")
	elementProp = etree.SubElement(httpSamplerProxy, "elementProp")
	elementProp.set("name", "HTTPsampler.Arguments")
	elementProp.set("elementType", "Arguments")
	boolProp(elementProp, "HTTPArgument.always_encode", "false")
	stringProp(elementProp, "Argument.value", data)
	stringProp(elementProp, "Argument.metadata", "=")

class JmeterGen():
	def __init__(self):
		self.root = jmeterTestPlan()
		t1 = hashTree(self.root)
		testPlan(t1)
		t2 = hashTree(t1)
		t3 = resultCollector(t2)
		hashTree(t2)
		headerManager(t2)
		hashTree(t2)
		threadGroup(t2)
		self.t3 = hashTree(t2)

	def __str__(self):
		return etree.tostring(self.root, pretty_print=True).decode()

	def request(self, name, url, data="{}"):
		httpSamplerProxy(self.t3, name, url, data)
		hashTree(self.t3)

	def save(self, f):
		tree = etree.ElementTree(self.root)
		tree.write(f, pretty_print=True, xml_declaration=True, encoding='utf-8')
		print("save:", f)
