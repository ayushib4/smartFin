import 'package:flutter/material.dart';
import 'package:smart_fin_flutter/screens/agent.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

Future main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  await dotenv.load(fileName: ".env");
  runApp(const SmartFin());
}

class SmartFin extends StatelessWidget {
  const SmartFin({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'SmartFin',
      theme: ThemeData(
        colorScheme: const ColorScheme.dark(background: Colors.black),
        useMaterial3: true,
      ),
      home: const Agent(
        mood: "sad",
      ),
    );
  }
}
