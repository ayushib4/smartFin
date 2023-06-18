import 'package:flutter/material.dart';
import 'dart:async';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:plaid_flutter/plaid_flutter.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  LinkConfiguration? _configuration;
  StreamSubscription<LinkEvent>? _streamEvent;
  StreamSubscription<LinkExit>? _streamExit;
  StreamSubscription<LinkSuccess>? _streamSuccess;
  // LinkObject? _successObject;
  String linkToken = "";
  String accessToken = "";

  @override
  void initState() {
    super.initState();

    createLinkToken();

    _streamEvent = PlaidLink.onEvent.listen(_onEvent);
    _streamExit = PlaidLink.onExit.listen(_onExit);
    _streamSuccess = PlaidLink.onSuccess.listen(_onSuccess);
  }

  void createLinkToken() async {
    http.Response response = await http.post(
      Uri.parse('https://sandbox.plaid.com/link/token/create'),
      headers: <String, String>{
        'Content-Type': 'application/json',
      },
      body: jsonEncode({
        'client_id': dotenv.env["PLAID_CLIENT_ID"].toString(),
        'secret': dotenv.env["PLAID_SECRET"].toString(),
        'user': {'client_user_id': 'unique-per-user'},
        'client_name': 'SmartFin',
        'products': ['auth', 'transactions'],
        'country_codes': ['US'],
        'language': 'en',
        'android_package_name': 'com.example.smart_fin_flutter',
        'account_filters': {
          'depository': {
            'account_subtypes': ['checking'],
          },
        },
      }),
    );

    if (response.statusCode == 200) {
      linkToken = await jsonDecode(response.body)['link_token'];
    } else {
      print(response.body);
    }
  }

  @override
  void dispose() {
    _streamEvent?.cancel();
    _streamExit?.cancel();
    _streamSuccess?.cancel();
    super.dispose();
  }

  void _createLinkTokenConfiguration() {
    _configuration = LinkTokenConfiguration(
      token: linkToken,
    );

    PlaidLink.open(configuration: _configuration!);
  }

  void _onEvent(LinkEvent event) {
    // final name = event.name;
    // final metadata = event.metadata.description();
    // print("onEvent: $name, metadata: $metadata");
  }

  void _onSuccess(LinkSuccess event) async {
    final token = event.publicToken;

    http.Response response = await http.post(
      Uri.parse('https://sandbox.plaid.com/item/public_token/exchange'),
      headers: <String, String>{
        'Content-Type': 'application/json',
      },
      body: jsonEncode({
        'client_id': dotenv.env["PLAID_CLIENT_ID"].toString(),
        'secret': dotenv.env["PLAID_SECRET"].toString(),
        'public_token': token,
      }),
    );

    if (response.statusCode == 200) {
      accessToken = await jsonDecode(response.body)['access_token'];
      // print("Access token: $accessToken");
    } else {
      print(response.body);
    }

    // final metadata = event.metadata.description();
    // print("onSuccess: $token, metadata: $metadata");
    // _successObject = event;
  }

  void _onExit(LinkExit event) {
    // final metadata = event.metadata.description();
    // final error = event.error?.description();
    // print("onExit metadata: $metadata, error: $error");
  }

  void getTransactions() async {
    http.Response response = await http.post(
      Uri.parse('https://sandbox.plaid.com/transactions/get'),
      headers: <String, String>{
        'Content-Type': 'application/json',
      },
      body: jsonEncode({
        'client_id': dotenv.env["PLAID_CLIENT_ID"].toString(),
        'secret': dotenv.env["PLAID_SECRET"].toString(),
        'access_token': accessToken,
        'start_date': '2018-01-01',
        'end_date': '2023-01-01',
        'options': {
          'count': 250,
          'offset': 100,
          'include_personal_finance_category': true,
        },
      }),
    );
    var transactions = jsonDecode(response.body)['transactions'];
    print("TRANSACTION DATA:\n$transactions");
  }

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Padding(
                padding: EdgeInsets.all(16.0),
                child: Text(
                  "SmartFin",
                  style: TextStyle(
                    fontSize: 48,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.fromLTRB(16.0, 0, 16.0, 16.0),
                child: ElevatedButton(
                  onPressed: _createLinkTokenConfiguration,
                  child: const Text("Sign in with Plaid"),
                ),
              ),
              Padding(
                padding: const EdgeInsets.fromLTRB(16.0, 0, 16.0, 16.0),
                child: ElevatedButton(
                  onPressed: () => getTransactions(),
                  child: const Text("Get Transactions"),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
