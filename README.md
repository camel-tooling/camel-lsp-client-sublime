# Camel LSP client for Sublime

The idea is to leverage the [Sublime LSP package](https://github.com/tomv564/LSP).

## Download Sublime

Download from [SublimeText 4 page](https://www.sublimetext.com/download)

# Camel Language Server Support Demo for XML

For instance, code completion for Camel XML.

![Demo](images/xmlsublime.gif)

# Camel Language Server Support Demo for JAVA

For instance, code completion for Camel JAVA.
![Demo](images/javasublime.gif)


## Install LSP plugin

- Tools -> Command palette... -> Package Control: Install Package
- Tools -> Command palette... -> Install LSP

## Configure LSP plugin for Camel

- Download Camel LSP server jar from (https://jar-download.com/artifacts/com.github.camel-tooling/camel-lsp-server/1.6.0/source-code)
- Preferences: Package Setting -> LSP Settings
- Fill `LSP.sublime-settings` with the following configuration and also please update path to the camel-lsp-server jar
```json
{

	"clients":
	{
		"Camel":
		{
			"command":
			[
				"java",
				"-jar",
				"PATH/TO/camel-lsp-server-1.6.0.jar"
			],
			"enabled": true,
			"languages": [
				{
					"selector": "text.xml",
					"priority_selector": "text.xml",
				},
				{
					"selector": "source.java",
					"priority_selector": "source.java",
				}
			],
		},
	},
}
```
## Follow these steps to automatically download the latest Apache Camel language server jar and create required LSP configurations. 

- Run the following command in your terminal. Open a `.java` or `.xml` in your sublime text to enable camel language server 

> Download and install a recent Java Development Kit
  
>	Java must be added to the system path
	
 
```
git clone https://github.com/camel-tooling/camel-lsp-client-sublime.git ~/.config/sublime-text/Packages/LSP-camel
```
Enjoy the Completion of Camel URI in Sublime.
