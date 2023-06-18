// import 'dart:developer';
import 'dart:math';
import 'package:flutter/material.dart';
import 'package:smart_fin_flutter/screens/agent.dart';
// import 'package:http/http.dart' as http;

class User extends StatefulWidget {
  const User({super.key});

  @override
  State<User> createState() => _UserState();
}

class _UserState extends State<User> {
  final _formKey = GlobalKey<FormState>();

  void submitForm() async {
    // http.Response response = await http.post(
    //   Uri.parse('http://10.165.1.120:5000/agent-observe'),
    //   headers: <String, String>{
    //     'Content-Type': 'text/plain',
    //   },
    // );

    // log(jsonDecode(response.body));

    var respToPick = Random().nextInt(2);

    if (_formKey.currentState!.validate()) {
      goToAgent(
          "angry",
          respToPick == 0
              ? "You spent over \$1K at Abercrombie & Fitch this month. Try cutting back on shopping for non-essentials."
              : "You spent a reasonable amount on food and transportation this month, but you could've saved more on late-night Uber rides.");
    }
  }

  void goToAgent(String mood, String response) {
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => Agent(
          mood: mood,
          response: response,
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Padding(
              padding: EdgeInsets.all(16.0),
              child: Text(
                "Tell us about yourself",
                style: TextStyle(
                  fontSize: 30.0,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
              child: Form(
                key: _formKey,
                child: Column(
                  children: [
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
                      child: TextFormField(
                        decoration: const InputDecoration(
                          hintText: "What's your name?",
                        ),
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter some text';
                          }
                          return null;
                        },
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
                      child: TextFormField(
                        keyboardType: TextInputType.number,
                        decoration: const InputDecoration(
                          hintText: "How old are you?",
                        ),
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter some text';
                          }
                          return null;
                        },
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
                      child: TextFormField(
                        decoration: const InputDecoration(
                          hintText: "What are your short-term financial goals?",
                        ),
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter some text';
                          }
                          return null;
                        },
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
                      child: TextFormField(
                        decoration: const InputDecoration(
                          hintText: "What are your long-term financial goals?",
                        ),
                        validator: (value) {
                          if (value == null || value.isEmpty) {
                            return 'Please enter some text';
                          }
                          return null;
                        },
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(16.0, 16.0, 16.0, 8.0),
                      child: ElevatedButton(
                        onPressed: () => submitForm(),
                        child: const Text("Submit"),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
